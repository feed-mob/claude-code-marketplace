#!/usr/bin/env ruby
# frozen_string_literal: true

require 'csv'
require 'uri'
require 'cgi'
require 'fileutils'

# Extracts all query parameters from a URL, returning a Hash of { param_name => [values] }.
def extract_query_params(url)
  return {} if url.nil? || url.strip.empty?

  uri = URI.parse(url)
  return {} if uri.query.nil?

  params = Hash.new { |hash, key| hash[key] = [] }
  URI.decode_www_form(uri.query).each do |key, value|
    params[key] << value
  end
  params
rescue URI::InvalidURIError
  {}
end

# Process CSV files and extract URL parameters
def process_csv_files(csv_paths = nil)
  # If no specific files provided, process all CSV files in current directory
  csv_files = csv_paths || Dir.glob('*.csv')

  if csv_files.empty?
    puts "No CSV files found to process."
    return
  end

  csv_files.each do |csv_path|
    puts "Processing #{csv_path}..."

    begin
      table = CSV.read(csv_path, headers: true)
      original_headers = table.headers
      row_params = []
      param_names = []

      # Find URL column (case insensitive)
      url_column = nil
      ['url', 'URL'].each do |col|
        if original_headers.include?(col)
          url_column = col
          break
        end
      end

      unless url_column
        puts "Warning: No 'url' or 'URL' column found in #{csv_path}. Skipping."
        next
      end

      # Extract parameters from each URL
      table.each do |row|
        params = extract_query_params(row[url_column])
        row_params << params
        params.each_key do |key|
          param_names << key unless param_names.include?(key)
        end
      end

      if param_names.empty?
        puts "No URL parameters found in #{csv_path}. Skipping."
        next
      end

      # Ensure we don't duplicate existing headers
      new_param_headers = param_names.reject { |name| original_headers.include?(name) }
      combined_headers = original_headers + new_param_headers

      # Create temporary file
      tmp_path = "#{csv_path}.tmp"

      CSV.open(tmp_path, 'w', write_headers: true, headers: combined_headers) do |csv|
        table.each_with_index do |row, index|
          params = row_params[index]

          csv << combined_headers.map do |header|
            if original_headers.include?(header)
              row[header]
            else
              values = params[header]
              values&.join('|')
            end
          end
        end
      end

      # Replace original file with processed version
      FileUtils.mv(tmp_path, csv_path)
      puts "Successfully processed #{csv_path}. Added #{new_param_headers.length} parameter columns: #{new_param_headers.join(', ')}"

    rescue => e
      puts "Error processing #{csv_path}: #{e.message}"
    end
  end
end

# Main execution
if __FILE__ == $0
  # Allow command line arguments for specific files
  specific_files = ARGV.any? ? ARGV : nil
  process_csv_files(specific_files)
end
