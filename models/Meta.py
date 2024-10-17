from dataclasses import dataclass


@dataclass
class Meta:
    createdAt: str
    updatedAt: str
    barcode: str
    qr_code: str