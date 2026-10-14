import hashlib as hasher

from datetime import datetime
from typing import Any


class Block:
    def __init__(self, indeks: int, cap_waktu: datetime, data: Any, previous_hash: str) -> None:
        self.indeks = indeks
        self.cap_waktu = cap_waktu
        self.data = data
        self.previous_hash = previous_hash
        
        
        self.hash_block = self._hitung_hash_block()
        
    def _hitung_hash_block(self) -> str:
        # Implementasi perhitungan hash untuk blok
        # Misalnya menggunakan SHA-256
        sha = hasher.sha256()
        isi_block = (
            str(self.indeks) +
            str(self.cap_waktu) +
            str(self.data) +
            str(self.previous_hash) 
        )
        
        sha.update(isi_block.encode('utf-8'))
        return sha.hexdigest()
    
def buat_block_gensis() -> Block:
        # Implementasi pembuatan blok baru
        return Block(
            indeks=0,
            cap_waktu=datetime.now(),
            data="Blok Genesis pertama",
            previous_hash="0"
        )
        
def buat_block_baru(block_terakhir: Block) -> Block:
    indeks_baru = block_terakhir.indeks + 1
    cap_waktu_baru = datetime.now()
    data_baru = f"Blok baru dengan indeks {indeks_baru}."
    hash_sebelumnya = block_terakhir.hash_block
    
    return Block(
        indeks=indeks_baru,
        cap_waktu=cap_waktu_baru,
        data=data_baru,
        previous_hash=hash_sebelumnya
    ) 
    
if __name__ == "__main__":
    rantai_block = [buat_block_gensis()]
    blok_sebelumnya = rantai_block[0]
    
    jumlah_block_baru = 5
    for i in range(jumlah_block_baru):
        blok_baru: Block = buat_block_baru(blok_sebelumnya)
        rantai_block.append(blok_baru)
        blok_sebelumnya = blok_baru
        
        print(f"Blok {blok_baru.indeks} dibuat dengan hash: {blok_baru.hash_block} telah ditambahkan ke rantai.")
    
    
        