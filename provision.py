

from ndef import *
from config import *
from modulereader_client import read_uid , write_chunks_to_pages , wait_for_removal
from supabase_client import insert_card 



while True:
    uid = read_uid()
    if uid is None:
        continue


    url = BASE_URL+uid
    ndef_bytes = build_uri_record(url)
    tlv_bytes = wrap_TLV(ndef_bytes)
    chunks = chunk_pages(tlv_bytes)



    try:


        write_chunks_to_pages(chunks)

        #supabase - database record
        insert_card(uid)

        print(f"[PROVISION] ✅ {uid}, proivisioned")
    except Exception as e:
        print(f"[PROVISION] ❌ Error : {e}")






    wait_for_removal()