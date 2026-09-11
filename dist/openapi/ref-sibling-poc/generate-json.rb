#!/usr/bin/env ruby

require 'json'
require 'yaml'

Dir.glob(File.join(__dir__, '*-openapi-*.yaml')).sort.each do |yaml_path|
  json_path = yaml_path.sub(/\.yaml\z/, '.json')
  document = YAML.load_file(yaml_path)

  File.write(json_path, "#{JSON.pretty_generate(document)}\n")
  puts File.basename(json_path)
end
