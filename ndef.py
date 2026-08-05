


url = "https://loyal-gold.vercel.app/pass/04a2913c"

#for URI record
header_flag = bytes([0xD1])
#how many bytes in this type - URI record
type_length = bytes([0x01])
#type of field content
record_type = bytes([0x55])

#NDEF record bytes
def build_uri_record(url , header_flag , type_length , record_type):

    prefix_code= 0x04
    #function received url and replaces prefix - replace https:// with blank
    remainder = url.replace("https://" , "")

    #convert remainder to bytes
    remainder_bytes = remainder.encode("utf-8")
    #payload back with bytes for prefix + remainder
    payload = bytes([prefix_code]) + remainder_bytes

    payload_length = bytes([len(payload)])

    final_payload = header_flag + type_length + payload_length + record_type + payload

    return final_payload

#TLV-wrapped bytes
def wrap_TLV(ndef_bytes):
    tlv_type = bytes([0x03])
    tlv_length = bytes([len(ndef_bytes)])
    tlv_terminator = bytes([0xFe])

    tlv_message = tlv_type + tlv_length + ndef_bytes + tlv_terminator

    return tlv_message

#4-byte page chuhks - ready for client to write
def chunk_pages(data):
    #empty array to store
    chunks = []


    for i in range(0,len(data), 4):
        chunk = data[i : i+4]
        chunks.append(chunk)

        #padding for chunks with less than 4
        #only happens for last set
        last_chunk= chunks[-1]
        #if its less than 4
        if len(last_chunk) < 4:
            #check how much padding needed
            padding_needed = 4 - len(last_chunk)
            #where it is
            chunks[-1] = last_chunk + bytes(padding_needed)
 
    return chunks

result = build_uri_record(url , header_flag , type_length , record_type)
print(result)