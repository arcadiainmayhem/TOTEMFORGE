

from ndef import *
from config import *
from modulereader_client import read_uid , write_chunks_to_pages , wait_for_removal
from supabase_client import insert_card 



print(f"[PROVISION] Card Reader Ready : Place a card on the reader")


while True:
    uid = read_uid()
    if uid is None:
        continue

    print(f"[PROVISION] Card Detected - UID : {uid}")

    url = BASE_URL+uid

    print(f"[PROVISION] Current Url : {url}")
    ndef_bytes = build_uri_record(url , header_flag , type_length, record_type)
    tlv_bytes = wrap_TLV(ndef_bytes)
    chunks = chunk_pages(tlv_bytes)

    print(f"[PROVISION] Current Chunks: {chunks}")



    try:


        write_chunks_to_pages(chunks)

        #supabase - database record
        insert_card(uid)
        print(f"[PROVISION] Supabase Record created")

        print(f"[PROVISION] ✅ {uid}, proivisioned")
    except Exception as e:
        print(f"[PROVISION] ❌ Error : {e}")






    wait_for_removal()
    print(f"[PROVISION] 🟢 Ready. Place next card.")