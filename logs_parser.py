
def parse_protocol_mapping():

  """
  Parses the protocols.txt file which contains 
  mapping of protocol number to the keyword.
  The file is present in the current directory itself.

  Input:
  None

  Returns:
  Map of protocol number as key and keyword as value
  
  For eg :
  {
  '0' : 'hopopt',
  '1' : 'icmp'
  }

  """

  protocol_keyword_map = {}

  with open("./protocols.txt","r") as file:
    for line in file:
      line = line.strip()
      line = line.split()

      # This check is to avoid out of index exception.
      if len(line)<2:
        continue

      protocol_keyword_map[line[0]] = line[1].lower()

  return protocol_keyword_map  


def parse_log_file(log_file_path,protocol_num_map):

  """
  Parses the flow log data file. The parsed file is 
  returned as a map for easier computations and better
  runtime efficiency.

  Input:
  1. Path to the flow log data file
  2. Mapping of protocol number to keyword mapping

  Returns:
  Map of dstPort and protocol keyword seperated by hyphen (-) as key 
  and their count as value
  
  For eg :
  {
  '49153-tcp': 1, 
  '49154-tcp': 2,
  }

  """

  header_exist = "version"
  port_protocol_count = {}
  
  try : 
    with open(log_file_path,"r") as file:
      for line in file:
        line = line.strip()

        if header_exist in line:
          continue

        # This is is done to avoid any out of index error.
        if len(line)<8:
          continue

        line = line.split()

        port_protocol_count[line[6]+'-'+protocol_num_map.get(line[7])] = port_protocol_count.get(line[6]+'-'+protocol_num_map.get(line[7]),0) + 1

  except Exception as e:
    raise RuntimeError(f"An unexpected error occurred: {e}")

  return port_protocol_count


def parse_mapping_file(mapping_file_path):

  """
  Parses the lookup table file. The parsed file is returned
  as a map which is used to find the corresponding tags
  for protocol port combinations.

  Input:
  1. Path to the lookup table file.

  Returns:
  Map of port and protocol seperated by hyphen (-) as key
  and their tag as value
  
  For eg :
  {
  '25-tcp' : 'sv_P1' ,
  '3389-tcp: 'sv_P5'
  }

  """

  header_exist = "dstport"
  tags_map = {}

  try :
    with open(mapping_file_path,"r") as file:
      for line in file:
        line = line.strip()

        if header_exist in line:
          continue

        line = line.split(",")


        if len(line)<3:
          continue

        tags_map[line[0]+'-'+line[1].lower()] = line[2]

  except Exception as e:
    raise RuntimeError(f"An unexpected error occurred: {e}")

  return tags_map

def generate_output(protocol_port_count,tags_map):

  """
  Generates the output data i.e the count of matches for each tags
  and count of matches for each port protocol combination. The key 
  from log file correspond to key in table lookup, so we can directly
  use that to get their count.

  Input:
  1. Map of (destPort - Protocol) and their count in log file 
  2. Map of (Port - Protocol) and their tag 

  Returns:
  None

  """

  tag_count = {}

  for key in protocol_port_count:
    if key in tags_map:
      tag = tags_map[key]
      tag_count[tag] = tag_count.get(tag,0) + protocol_port_count[key]
    else:
      tag_count['Untagged'] = tag_count.get('Untagged',0) + protocol_port_count[key]


  write_tag_count("tag_count.txt",tag_count)
  write_combination_count("combination_count.txt",protocol_port_count)


def write_tag_count(file_name,output_data):
  """
  Writes the tags and their counts in an output file.

  Input:
  1. Name of the output file for tag count
  2. Map of tag as key and their count as value

  Returns:
  None

  """

  try:

      with open(file_name, mode='w') as file:
        file.write('Tag,Count'+'\n')

        for key in output_data:

            # Join for given row by commas and write to file
            file.write(key+',' + str(output_data.get(key)) + '\n')

      print(f"Data successfully written to {file_name}")

  except Exception as e:
    raise RuntimeError(f"An error occurred while writing to the file: {e}")




def write_combination_count(file_name,output_data):

  """
  Writes the port/protocol and their counts in an output file.

  Input:
  1. Name of the output file for port/protocol count
  2. Map of (port - protocol) as key and their count as value

  Returns:
  None

  """

  try:
      
      with open(file_name, mode='w') as file:
        file.write('Port,Protocol,Count'+'\n')

        for key in output_data:
            destPort_protocol = key.split('-')
            port = destPort_protocol[0]
            protocol = destPort_protocol[1]

            # Join for given row by commas and write to file
            file.write(port +','+ protocol +',' + str(output_data.get(key)) + '\n')

      print(f"Data successfully written to {file_name}")
      
  except Exception as e:
    raise RuntimeError(f"An error occurred while writing to the file: {e}")


def main():
  
  log_file_path = input("Enter the log file path: ")
  mapping_file_path = input("Enter the look up data file path: ")

  # Parsing the Protocol to Keyword File
  port_protocol_count  = parse_protocol_mapping()

  # Parsing the input log file
  protocol_port_count = parse_log_file(log_file_path,port_protocol_count)

  #Parse look up table data file
  tags_map = parse_mapping_file(mapping_file_path)

  # Finding the output and Generating the output files
  generate_output(protocol_port_count,tags_map)

if __name__ == "__main__":
  
  main()

