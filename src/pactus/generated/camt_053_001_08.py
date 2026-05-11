from __future__ import annotations

from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod
from xsdata_pydantic.fields import field

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08"


class AccountSchemeName1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class ActiveCurrencyAndAmount(BaseModel):
    model_config = ConfigDict(defer_build=True)
    value: Decimal = field(
        metadata={
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        }
    )
    ccy: str = field(
        metadata={
            "name": "Ccy",
            "type": "Attribute",
            "pattern": r"[A-Z]{3,3}",
        }
    )


class ActiveOrHistoricCurrencyAnd13DecimalAmount(BaseModel):
    model_config = ConfigDict(defer_build=True)
    value: Decimal = field(
        metadata={
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 13,
        }
    )
    ccy: str = field(
        metadata={
            "name": "Ccy",
            "type": "Attribute",
            "pattern": r"[A-Z]{3,3}",
        }
    )


class ActiveOrHistoricCurrencyAndAmount(BaseModel):
    model_config = ConfigDict(defer_build=True)
    value: Decimal = field(
        metadata={
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        }
    )
    ccy: str = field(
        metadata={
            "name": "Ccy",
            "type": "Attribute",
            "pattern": r"[A-Z]{3,3}",
        }
    )


class AddressType2Code(Enum):
    ADDR = "ADDR"
    PBOX = "PBOX"
    HOME = "HOME"
    BIZZ = "BIZZ"
    MLTO = "MLTO"
    DLVY = "DLVY"


class AmountRangeBoundary1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    bdry_amt: Decimal = field(
        metadata={
            "name": "BdryAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        }
    )
    incl: bool = field(
        metadata={
            "name": "Incl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )


class AttendanceContext1Code(Enum):
    ATTD = "ATTD"
    SATT = "SATT"
    UATT = "UATT"


class AuthenticationEntity1Code(Enum):
    ICCD = "ICCD"
    AGNT = "AGNT"
    MERC = "MERC"


class AuthenticationMethod1Code(Enum):
    UKNW = "UKNW"
    BYPS = "BYPS"
    NPIN = "NPIN"
    FPIN = "FPIN"
    CPSG = "CPSG"
    PPSG = "PPSG"
    MANU = "MANU"
    MERC = "MERC"
    SCRT = "SCRT"
    SNCT = "SNCT"
    SCNL = "SCNL"


class BalanceSubType1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class BalanceType10Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class BankTransactionCodeStructure6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: str = field(
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        }
    )
    sub_fmly_cd: str = field(
        metadata={
            "name": "SubFmlyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        }
    )


class Cscmanagement1Code(Enum):
    PRST = "PRST"
    BYPS = "BYPS"
    UNRD = "UNRD"
    NCSC = "NCSC"


class CardDataReading1Code(Enum):
    TAGC = "TAGC"
    PHYS = "PHYS"
    BRCD = "BRCD"
    MGST = "MGST"
    CICC = "CICC"
    DFLE = "DFLE"
    CTLS = "CTLS"
    ECTL = "ECTL"


class CardPaymentServiceType2Code(Enum):
    AGGR = "AGGR"
    DCCV = "DCCV"
    GRTT = "GRTT"
    INSP = "INSP"
    LOYT = "LOYT"
    NRES = "NRES"
    PUCO = "PUCO"
    RECP = "RECP"
    SOAF = "SOAF"
    UNAF = "UNAF"
    VCAU = "VCAU"


class CardSequenceNumberRange1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    frst_tx: None | str = field(
        default=None,
        metadata={
            "name": "FrstTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    last_tx: None | str = field(
        default=None,
        metadata={
            "name": "LastTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class CardholderVerificationCapability1Code(Enum):
    MNSG = "MNSG"
    NPIN = "NPIN"
    FCPN = "FCPN"
    FEPN = "FEPN"
    FDSG = "FDSG"
    FBIO = "FBIO"
    MNVR = "MNVR"
    FBIG = "FBIG"
    APKI = "APKI"
    PKIS = "PKIS"
    CHDT = "CHDT"
    SCEC = "SCEC"


class CashAccountType2Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class CashAvailabilityDate1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    nb_of_days: None | str = field(
        default=None,
        metadata={
            "name": "NbOfDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[\+]{0,1}[0-9]{1,15}",
        },
    )
    actl_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "ActlDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class ChargeBearerType1Code(Enum):
    DEBT = "DEBT"
    CRED = "CRED"
    SHAR = "SHAR"
    SLEV = "SLEV"


class ClearingSystemIdentification2Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class CopyDuplicate1Code(Enum):
    CODU = "CODU"
    COPY = "COPY"
    DUPL = "DUPL"


class CorporateAction9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    evt_tp: str = field(
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    evt_id: str = field(
        metadata={
            "name": "EvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )


class CreditDebitCode(Enum):
    CRDT = "CRDT"
    DBIT = "DBIT"


class CreditLineType1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class CurrencyExchange5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    src_ccy: str = field(
        metadata={
            "name": "SrcCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[A-Z]{3,3}",
        }
    )
    trgt_ccy: None | str = field(
        default=None,
        metadata={
            "name": "TrgtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    unit_ccy: None | str = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Decimal = field(
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        }
    )
    ctrct_id: None | str = field(
        default=None,
        metadata={
            "name": "CtrctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    qtn_dt: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "QtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class DateAndDateTime2Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    dt_tm: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class DateAndPlaceOfBirth1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    birth_dt: XmlDate = field(
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    prvc_of_birth: None | str = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: str = field(
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    ctry_of_birth: str = field(
        metadata={
            "name": "CtryOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[A-Z]{2,2}",
        }
    )


class DatePeriod2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    fr_dt: XmlDate = field(
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    to_dt: XmlDate = field(
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )


class DateTimePeriod1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    fr_dt_tm: XmlDateTime = field(
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    to_dt_tm: XmlDateTime = field(
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )


class DiscountAmountType1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class DocumentLineType1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class DocumentType3Code(Enum):
    RADM = "RADM"
    RPIN = "RPIN"
    FXDR = "FXDR"
    DISP = "DISP"
    PUOR = "PUOR"
    SCOR = "SCOR"


class DocumentType6Code(Enum):
    MSIN = "MSIN"
    CNFA = "CNFA"
    DNFA = "DNFA"
    CINV = "CINV"
    CREN = "CREN"
    DEBN = "DEBN"
    HIRI = "HIRI"
    SBIN = "SBIN"
    CMCN = "CMCN"
    SOAC = "SOAC"
    DISP = "DISP"
    BOLD = "BOLD"
    VCHR = "VCHR"
    AROI = "AROI"
    TSUT = "TSUT"
    PUOR = "PUOR"


class EntryStatus1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class FinancialIdentificationSchemeName1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class FinancialInstrumentQuantity1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    unit: None | Decimal = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: None | Decimal = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    amtsd_val: None | Decimal = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


class GarnishmentType1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class GenericIdentification1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    schme_nm: None | str = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: None | str = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class GenericIdentification3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    issr: None | str = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class GenericIdentification30(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[a-zA-Z0-9]{4}",
        }
    )
    issr: str = field(
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    schme_nm: None | str = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class IdentificationSource3Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class InterestType1Code(Enum):
    INDY = "INDY"
    OVRN = "OVRN"


class LocalInstrument2Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class MessageIdentification2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    msg_nm_id: None | str = field(
        default=None,
        metadata={
            "name": "MsgNmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_id: None | str = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class NamePrefix2Code(Enum):
    DOCT = "DOCT"
    MADM = "MADM"
    MISS = "MISS"
    MIST = "MIST"
    MIKS = "MIKS"


class NumberAndSumOfTransactions1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    nb_of_ntries: None | str = field(
        default=None,
        metadata={
            "name": "NbOfNtries",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[0-9]{1,15}",
        },
    )
    sum: None | Decimal = field(
        default=None,
        metadata={
            "name": "Sum",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


class OnLineCapability1Code(Enum):
    OFLN = "OFLN"
    ONLN = "ONLN"
    SMON = "SMON"


class OrganisationIdentificationSchemeName1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class OriginalAndCurrentQuantities1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    face_amt: Decimal = field(
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        }
    )
    amtsd_val: Decimal = field(
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        }
    )


class OriginalBusinessQuery1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    msg_id: str = field(
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    msg_nm_id: None | str = field(
        default=None,
        metadata={
            "name": "MsgNmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class OtherContact1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    chanl_tp: str = field(
        metadata={
            "name": "ChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 128,
        },
    )


class PoicomponentType1Code(Enum):
    SOFT = "SOFT"
    EMVK = "EMVK"
    EMVO = "EMVO"
    MRIT = "MRIT"
    CHIT = "CHIT"
    SECM = "SECM"
    PEDV = "PEDV"


class Pagination1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    pg_nb: str = field(
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[0-9]{1,5}",
        }
    )
    last_pg_ind: bool = field(
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )


class PartyType3Code(Enum):
    OPOI = "OPOI"
    MERC = "MERC"
    ACCP = "ACCP"
    ITAG = "ITAG"
    ACQR = "ACQR"
    CISS = "CISS"
    DLIS = "DLIS"


class PartyType4Code(Enum):
    MERC = "MERC"
    ACCP = "ACCP"
    ITAG = "ITAG"
    ACQR = "ACQR"
    CISS = "CISS"
    TAXH = "TAXH"


class PersonIdentificationSchemeName1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class PreferredContactMethod1Code(Enum):
    LETT = "LETT"
    MAIL = "MAIL"
    PHON = "PHON"
    FAXX = "FAXX"
    CELL = "CELL"


class PriceValueType1Code(Enum):
    DISC = "DISC"
    PREM = "PREM"
    PARV = "PARV"


class ProprietaryBankTransactionCodeStructure1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: str = field(
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    issr: None | str = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class ProprietaryQuantity1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tp: str = field(
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    qty: str = field(
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )


class ProprietaryReference1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tp: str = field(
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    ref: str = field(
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )


class ProxyAccountType1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class Purpose2Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class RateType4Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    pctg: None | Decimal = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    othr: None | str = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class RemittanceLocationMethod2Code(Enum):
    FAXI = "FAXI"
    EDIC = "EDIC"
    URID = "URID"
    EMAL = "EMAL"
    POST = "POST"
    SMSM = "SMSM"


class ReportingSource1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class ReturnReason5Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class SequenceRange1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    fr_seq: str = field(
        metadata={
            "name": "FrSeq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    to_seq: str = field(
        metadata={
            "name": "ToSeq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )


class SupplementaryDataEnvelope1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


class TaxAmountType1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class TaxAuthorisation1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    titl: None | str = field(
        default=None,
        metadata={
            "name": "Titl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: None | str = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )


class TaxParty1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tax_id: None | str = field(
        default=None,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    regn_id: None | str = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_tp: None | str = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class TaxRecordPeriod1Code(Enum):
    MM01 = "MM01"
    MM02 = "MM02"
    MM03 = "MM03"
    MM04 = "MM04"
    MM05 = "MM05"
    MM06 = "MM06"
    MM07 = "MM07"
    MM08 = "MM08"
    MM09 = "MM09"
    MM10 = "MM10"
    MM11 = "MM11"
    MM12 = "MM12"
    QTR1 = "QTR1"
    QTR2 = "QTR2"
    QTR3 = "QTR3"
    QTR4 = "QTR4"
    HLF1 = "HLF1"
    HLF2 = "HLF2"


class TechnicalInputChannel1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class TrackData1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    trck_nb: None | str = field(
        default=None,
        metadata={
            "name": "TrckNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[0-9]",
        },
    )
    trck_val: str = field(
        metadata={
            "name": "TrckVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 140,
        }
    )


class TransactionChannel1Code(Enum):
    MAIL = "MAIL"
    TLPH = "TLPH"
    ECOM = "ECOM"
    TVPY = "TVPY"


class TransactionEnvironment1Code(Enum):
    MERC = "MERC"
    PRIV = "PRIV"
    PUBL = "PUBL"


class TransactionIdentifier1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tx_dt_tm: XmlDateTime = field(
        metadata={
            "name": "TxDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    tx_ref: str = field(
        metadata={
            "name": "TxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )


class UnitOfMeasure1Code(Enum):
    PIEC = "PIEC"
    TONS = "TONS"
    FOOT = "FOOT"
    GBGA = "GBGA"
    USGA = "USGA"
    GRAM = "GRAM"
    INCH = "INCH"
    KILO = "KILO"
    PUND = "PUND"
    METR = "METR"
    CMET = "CMET"
    MMET = "MMET"
    LITR = "LITR"
    CELI = "CELI"
    MILI = "MILI"
    GBOU = "GBOU"
    USOU = "USOU"
    GBQA = "GBQA"
    USQA = "USQA"
    GBPI = "GBPI"
    USPI = "USPI"
    MILE = "MILE"
    KMET = "KMET"
    YARD = "YARD"
    SQKI = "SQKI"
    HECT = "HECT"
    ARES = "ARES"
    SMET = "SMET"
    SCMT = "SCMT"
    SMIL = "SMIL"
    SQMI = "SQMI"
    SQYA = "SQYA"
    SQFO = "SQFO"
    SQIN = "SQIN"
    ACRE = "ACRE"


class UserInterface2Code(Enum):
    MDSP = "MDSP"
    CDSP = "CDSP"


class AddressType3Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | AddressType2Code = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    prtry: None | GenericIdentification30 = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class AmountAndCurrencyExchangeDetails3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    amt: ActiveOrHistoricCurrencyAndAmount = field(
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    ccy_xchg: None | CurrencyExchange5 = field(
        default=None,
        metadata={
            "name": "CcyXchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class AmountAndCurrencyExchangeDetails4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tp: str = field(
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    amt: ActiveOrHistoricCurrencyAndAmount = field(
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    ccy_xchg: None | CurrencyExchange5 = field(
        default=None,
        metadata={
            "name": "CcyXchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class AmountAndDirection35(BaseModel):
    model_config = ConfigDict(defer_build=True)
    amt: Decimal = field(
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 17,
        }
    )
    cdt_dbt_ind: CreditDebitCode = field(
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )


class BalanceType13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd_or_prtry: BalanceType10Choice = field(
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    sub_tp: None | BalanceSubType1Choice = field(
        default=None,
        metadata={
            "name": "SubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class BankTransactionCodeStructure5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: str = field(
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        }
    )
    fmly: BankTransactionCodeStructure6 = field(
        metadata={
            "name": "Fmly",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )


class BatchInformation2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    msg_id: None | str = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pmt_inf_id: None | str = field(
        default=None,
        metadata={
            "name": "PmtInfId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nb_of_txs: None | str = field(
        default=None,
        metadata={
            "name": "NbOfTxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[0-9]{1,15}",
        },
    )
    ttl_amt: None | ActiveOrHistoricCurrencyAndAmount = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    cdt_dbt_ind: None | CreditDebitCode = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class CardSecurityInformation1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cscmgmt: Cscmanagement1Code = field(
        metadata={
            "name": "CSCMgmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    cscval: None | str = field(
        default=None,
        metadata={
            "name": "CSCVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[0-9]{3,4}",
        },
    )


class CardholderAuthentication2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    authntcn_mtd: AuthenticationMethod1Code = field(
        metadata={
            "name": "AuthntcnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    authntcn_ntty: AuthenticationEntity1Code = field(
        metadata={
            "name": "AuthntcnNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )


class CashAvailability1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dt: CashAvailabilityDate1Choice = field(
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    amt: ActiveOrHistoricCurrencyAndAmount = field(
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    cdt_dbt_ind: CreditDebitCode = field(
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )


class CashDeposit1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    note_dnmtn: ActiveCurrencyAndAmount = field(
        metadata={
            "name": "NoteDnmtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    nb_of_notes: str = field(
        metadata={
            "name": "NbOfNotes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[0-9]{1,15}",
        }
    )
    amt: ActiveCurrencyAndAmount = field(
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )


class ChargeType3Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: None | GenericIdentification3 = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class ClearingSystemMemberIdentification2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    clr_sys_id: None | ClearingSystemIdentification2Choice = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    mmb_id: str = field(
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )


class Contact4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    nm_prfx: None | NamePrefix2Code = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    nm: None | str = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: None | str = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: None | str = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: None | str = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: None | str = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    email_purp: None | str = field(
        default=None,
        metadata={
            "name": "EmailPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: None | str = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: None | str = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: None | str = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    othr: list[OtherContact1] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    prefrd_mtd: None | PreferredContactMethod1Code = field(
        default=None,
        metadata={
            "name": "PrefrdMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class CreditLine3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    incl: bool = field(
        metadata={
            "name": "Incl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    tp: None | CreditLineType1Choice = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    amt: None | ActiveOrHistoricCurrencyAndAmount = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    dt: None | DateAndDateTime2Choice = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class CreditorReferenceType1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | DocumentType3Code = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class DateOrDateTimePeriod1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dt: None | DatePeriod2 = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    dt_tm: None | DateTimePeriod1 = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class DiscountAmountAndType1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tp: None | DiscountAmountType1Choice = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    amt: ActiveOrHistoricCurrencyAndAmount = field(
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )


class DisplayCapabilities1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    disp_tp: UserInterface2Code = field(
        metadata={
            "name": "DispTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    nb_of_lines: str = field(
        metadata={
            "name": "NbOfLines",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[0-9]{1,3}",
        }
    )
    line_width: str = field(
        metadata={
            "name": "LineWidth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[0-9]{1,3}",
        }
    )


class DocumentAdjustment1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    amt: ActiveOrHistoricCurrencyAndAmount = field(
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    cdt_dbt_ind: None | CreditDebitCode = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rsn: None | str = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    addtl_inf: None | str = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )


class DocumentLineType1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd_or_prtry: DocumentLineType1Choice = field(
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    issr: None | str = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class FromToAmountRange1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    fr_amt: AmountRangeBoundary1 = field(
        metadata={
            "name": "FrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    to_amt: AmountRangeBoundary1 = field(
        metadata={
            "name": "ToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )


class GarnishmentType1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd_or_prtry: GarnishmentType1Choice = field(
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    issr: None | str = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class GenericAccountIdentification1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 34,
        }
    )
    schme_nm: None | AccountSchemeName1Choice = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    issr: None | str = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class GenericFinancialIdentification1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    schme_nm: None | FinancialIdentificationSchemeName1Choice = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    issr: None | str = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class GenericIdentification32(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    tp: None | PartyType3Code = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    issr: None | PartyType4Code = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    shrt_nm: None | str = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class GenericOrganisationIdentification1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    schme_nm: None | OrganisationIdentificationSchemeName1Choice = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    issr: None | str = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class GenericPersonIdentification1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    schme_nm: None | PersonIdentificationSchemeName1Choice = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    issr: None | str = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class InterestType1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | InterestType1Code = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class OtherIdentification1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    sfx: None | str = field(
        default=None,
        metadata={
            "name": "Sfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: IdentificationSource3Choice = field(
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )


class PointOfInteractionComponent1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    poicmpnt_tp: PoicomponentType1Code = field(
        metadata={
            "name": "POICmpntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    manfctr_id: None | str = field(
        default=None,
        metadata={
            "name": "ManfctrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mdl: None | str = field(
        default=None,
        metadata={
            "name": "Mdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    vrsn_nb: None | str = field(
        default=None,
        metadata={
            "name": "VrsnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 16,
        },
    )
    srl_nb: None | str = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    apprvl_nb: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ApprvlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )


class PriceRateOrAmount3Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    rate: None | Decimal = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: None | ActiveOrHistoricCurrencyAnd13DecimalAmount = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class Product2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    pdct_cd: str = field(
        metadata={
            "name": "PdctCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 70,
        }
    )
    unit_of_measr: None | UnitOfMeasure1Code = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    pdct_qty: None | Decimal = field(
        default=None,
        metadata={
            "name": "PdctQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    unit_pric: None | Decimal = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    pdct_amt: None | Decimal = field(
        default=None,
        metadata={
            "name": "PdctAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    tax_tp: None | str = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_pdct_inf: None | str = field(
        default=None,
        metadata={
            "name": "AddtlPdctInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class ProprietaryDate3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tp: str = field(
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    dt: DateAndDateTime2Choice = field(
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )


class ProprietaryPrice2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tp: str = field(
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    pric: ActiveOrHistoricCurrencyAndAmount = field(
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )


class ProxyAccountIdentification1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tp: None | ProxyAccountType1Choice = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 2048,
        }
    )


class ReferredDocumentType3Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd: None | DocumentType6Code = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    prtry: None | str = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class SecuritiesAccount19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    tp: None | GenericIdentification30 = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    nm: None | str = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )


class SequenceRange1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    fr_seq: None | str = field(
        default=None,
        metadata={
            "name": "FrSeq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    to_seq: None | str = field(
        default=None,
        metadata={
            "name": "ToSeq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fr_to_seq: list[SequenceRange1] = field(
        default_factory=list,
        metadata={
            "name": "FrToSeq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    eqseq: list[str] = field(
        default_factory=list,
        metadata={
            "name": "EQSeq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    neqseq: list[str] = field(
        default_factory=list,
        metadata={
            "name": "NEQSeq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class SupplementaryData1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    plc_and_nm: None | str = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: SupplementaryDataEnvelope1 = field(
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )


class TaxAmountAndType1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tp: None | TaxAmountType1Choice = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    amt: ActiveOrHistoricCurrencyAndAmount = field(
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )


class TaxCharges2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rate: None | Decimal = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: None | ActiveOrHistoricCurrencyAndAmount = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class TaxParty2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tax_id: None | str = field(
        default=None,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    regn_id: None | str = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_tp: None | str = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    authstn: None | TaxAuthorisation1 = field(
        default=None,
        metadata={
            "name": "Authstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class TaxPeriod2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    yr: None | XmlDate = field(
        default=None,
        metadata={
            "name": "Yr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    tp: None | TaxRecordPeriod1Code = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    fr_to_dt: None | DatePeriod2 = field(
        default=None,
        metadata={
            "name": "FrToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class TransactionQuantities3Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    qty: None | FinancialInstrumentQuantity1Choice = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    orgnl_and_cur_face_amt: None | OriginalAndCurrentQuantities1 = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    prtry: None | ProprietaryQuantity1 = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class TransactionReferences6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    msg_id: None | str = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr_ref: None | str = field(
        default=None,
        metadata={
            "name": "AcctSvcrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pmt_inf_id: None | str = field(
        default=None,
        metadata={
            "name": "PmtInfId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    instr_id: None | str = field(
        default=None,
        metadata={
            "name": "InstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    end_to_end_id: None | str = field(
        default=None,
        metadata={
            "name": "EndToEndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    uetr: None | str = field(
        default=None,
        metadata={
            "name": "UETR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}",
        },
    )
    tx_id: None | str = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mndt_id: None | str = field(
        default=None,
        metadata={
            "name": "MndtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chq_nb: None | str = field(
        default=None,
        metadata={
            "name": "ChqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clr_sys_ref: None | str = field(
        default=None,
        metadata={
            "name": "ClrSysRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_ownr_tx_id: None | str = field(
        default=None,
        metadata={
            "name": "AcctOwnrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr_tx_id: None | str = field(
        default=None,
        metadata={
            "name": "AcctSvcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: None | str = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcg_id: None | str = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry: list[ProprietaryReference1] = field(
        default_factory=list,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class YieldedOrValueType1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    yldd: None | bool = field(
        default=None,
        metadata={
            "name": "Yldd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    val_tp: None | PriceValueType1Code = field(
        default=None,
        metadata={
            "name": "ValTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class AccountIdentification4Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    iban: None | str = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: None | GenericAccountIdentification1 = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class AmountAndCurrencyExchange3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    instd_amt: None | AmountAndCurrencyExchangeDetails3 = field(
        default=None,
        metadata={
            "name": "InstdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    tx_amt: None | AmountAndCurrencyExchangeDetails3 = field(
        default=None,
        metadata={
            "name": "TxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    cntr_val_amt: None | AmountAndCurrencyExchangeDetails3 = field(
        default=None,
        metadata={
            "name": "CntrValAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    anncd_pstng_amt: None | AmountAndCurrencyExchangeDetails3 = field(
        default=None,
        metadata={
            "name": "AnncdPstngAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    prtry_amt: list[AmountAndCurrencyExchangeDetails4] = field(
        default_factory=list,
        metadata={
            "name": "PrtryAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class BankTransactionCodeStructure4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    domn: None | BankTransactionCodeStructure5 = field(
        default=None,
        metadata={
            "name": "Domn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    prtry: None | ProprietaryBankTransactionCodeStructure1 = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class CardAggregated2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    addtl_svc: None | CardPaymentServiceType2Code = field(
        default=None,
        metadata={
            "name": "AddtlSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    tx_ctgy: None | str = field(
        default=None,
        metadata={
            "name": "TxCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    sale_rcncltn_id: None | str = field(
        default=None,
        metadata={
            "name": "SaleRcncltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    seq_nb_rg: None | CardSequenceNumberRange1 = field(
        default=None,
        metadata={
            "name": "SeqNbRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    tx_dt_rg: None | DateOrDateTimePeriod1Choice = field(
        default=None,
        metadata={
            "name": "TxDtRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class CashBalance8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tp: BalanceType13 = field(
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    cdt_line: list[CreditLine3] = field(
        default_factory=list,
        metadata={
            "name": "CdtLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    amt: ActiveOrHistoricCurrencyAndAmount = field(
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    cdt_dbt_ind: CreditDebitCode = field(
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    dt: DateAndDateTime2Choice = field(
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    avlbty: list[CashAvailability1] = field(
        default_factory=list,
        metadata={
            "name": "Avlbty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class CreditorReferenceType2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd_or_prtry: CreditorReferenceType1Choice = field(
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    issr: None | str = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class DocumentLineIdentification1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tp: None | DocumentLineType1 = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    nb: None | str = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rltd_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "RltdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class ImpliedCurrencyAmountRange1Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    fr_amt: None | AmountRangeBoundary1 = field(
        default=None,
        metadata={
            "name": "FrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    to_amt: None | AmountRangeBoundary1 = field(
        default=None,
        metadata={
            "name": "ToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    fr_to_amt: None | FromToAmountRange1 = field(
        default=None,
        metadata={
            "name": "FrToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    eqamt: None | Decimal = field(
        default=None,
        metadata={
            "name": "EQAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    neqamt: None | Decimal = field(
        default=None,
        metadata={
            "name": "NEQAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


class NumberAndSumOfTransactions4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    nb_of_ntries: None | str = field(
        default=None,
        metadata={
            "name": "NbOfNtries",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[0-9]{1,15}",
        },
    )
    sum: None | Decimal = field(
        default=None,
        metadata={
            "name": "Sum",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    ttl_net_ntry: None | AmountAndDirection35 = field(
        default=None,
        metadata={
            "name": "TtlNetNtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class OrganisationIdentification29(BaseModel):
    model_config = ConfigDict(defer_build=True)
    any_bic: None | str = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: None | str = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: list[GenericOrganisationIdentification1] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class PaymentContext3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    card_pres: None | bool = field(
        default=None,
        metadata={
            "name": "CardPres",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    crdhldr_pres: None | bool = field(
        default=None,
        metadata={
            "name": "CrdhldrPres",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    on_line_cntxt: None | bool = field(
        default=None,
        metadata={
            "name": "OnLineCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    attndnc_cntxt: None | AttendanceContext1Code = field(
        default=None,
        metadata={
            "name": "AttndncCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    tx_envt: None | TransactionEnvironment1Code = field(
        default=None,
        metadata={
            "name": "TxEnvt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    tx_chanl: None | TransactionChannel1Code = field(
        default=None,
        metadata={
            "name": "TxChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    attndnt_msg_cpbl: None | bool = field(
        default=None,
        metadata={
            "name": "AttndntMsgCpbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    attndnt_lang: None | str = field(
        default=None,
        metadata={
            "name": "AttndntLang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[a-z]{2,2}",
        },
    )
    card_data_ntry_md: CardDataReading1Code = field(
        metadata={
            "name": "CardDataNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    fllbck_ind: None | bool = field(
        default=None,
        metadata={
            "name": "FllbckInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    authntcn_mtd: None | CardholderAuthentication2 = field(
        default=None,
        metadata={
            "name": "AuthntcnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class PersonIdentification13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dt_and_plc_of_birth: None | DateAndPlaceOfBirth1 = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    othr: list[GenericPersonIdentification1] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class PlainCardData1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    pan: str = field(
        metadata={
            "name": "PAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[0-9]{8,28}",
        }
    )
    card_seq_nb: None | str = field(
        default=None,
        metadata={
            "name": "CardSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[0-9]{2,3}",
        },
    )
    fctv_dt: None | XmlPeriod = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    xpry_dt: XmlPeriod = field(
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    svc_cd: None | str = field(
        default=None,
        metadata={
            "name": "SvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[0-9]{3}",
        },
    )
    trck_data: list[TrackData1] = field(
        default_factory=list,
        metadata={
            "name": "TrckData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    card_scty_cd: None | CardSecurityInformation1 = field(
        default=None,
        metadata={
            "name": "CardSctyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class PointOfInteractionCapabilities1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    card_rdng_cpblties: list[CardDataReading1Code] = field(
        default_factory=list,
        metadata={
            "name": "CardRdngCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    crdhldr_vrfctn_cpblties: list[CardholderVerificationCapability1Code] = field(
        default_factory=list,
        metadata={
            "name": "CrdhldrVrfctnCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    on_line_cpblties: None | OnLineCapability1Code = field(
        default=None,
        metadata={
            "name": "OnLineCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    disp_cpblties: list[DisplayCapabilities1] = field(
        default_factory=list,
        metadata={
            "name": "DispCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    prt_line_width: None | str = field(
        default=None,
        metadata={
            "name": "PrtLineWidth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[0-9]{1,3}",
        },
    )


class PostalAddress24(BaseModel):
    model_config = ConfigDict(defer_build=True)
    adr_tp: None | AddressType3Choice = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    dept: None | str = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: None | str = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: None | str = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: None | str = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: None | str = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    flr: None | str = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_bx: None | str = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: None | str = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: None | str = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: None | str = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    twn_lctn_nm: None | str = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstrct_nm: None | str = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: None | str = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: None | str = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


class Price7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tp: YieldedOrValueType1Choice = field(
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    val: PriceRateOrAmount3Choice = field(
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )


class ReferredDocumentType4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cd_or_prtry: ReferredDocumentType3Choice = field(
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    issr: None | str = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class RemittanceAmount2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    due_pybl_amt: None | ActiveOrHistoricCurrencyAndAmount = field(
        default=None,
        metadata={
            "name": "DuePyblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    dscnt_apld_amt: list[DiscountAmountAndType1] = field(
        default_factory=list,
        metadata={
            "name": "DscntApldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    cdt_note_amt: None | ActiveOrHistoricCurrencyAndAmount = field(
        default=None,
        metadata={
            "name": "CdtNoteAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    tax_amt: list[TaxAmountAndType1] = field(
        default_factory=list,
        metadata={
            "name": "TaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    adjstmnt_amt_and_rsn: list[DocumentAdjustment1] = field(
        default_factory=list,
        metadata={
            "name": "AdjstmntAmtAndRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rmtd_amt: None | ActiveOrHistoricCurrencyAndAmount = field(
        default=None,
        metadata={
            "name": "RmtdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class RemittanceAmount3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    due_pybl_amt: None | ActiveOrHistoricCurrencyAndAmount = field(
        default=None,
        metadata={
            "name": "DuePyblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    dscnt_apld_amt: list[DiscountAmountAndType1] = field(
        default_factory=list,
        metadata={
            "name": "DscntApldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    cdt_note_amt: None | ActiveOrHistoricCurrencyAndAmount = field(
        default=None,
        metadata={
            "name": "CdtNoteAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    tax_amt: list[TaxAmountAndType1] = field(
        default_factory=list,
        metadata={
            "name": "TaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    adjstmnt_amt_and_rsn: list[DocumentAdjustment1] = field(
        default_factory=list,
        metadata={
            "name": "AdjstmntAmtAndRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rmtd_amt: None | ActiveOrHistoricCurrencyAndAmount = field(
        default=None,
        metadata={
            "name": "RmtdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class SecurityIdentification19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    isin: None | str = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )


class TaxRecordDetails2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    prd: None | TaxPeriod2 = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    amt: ActiveOrHistoricCurrencyAndAmount = field(
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )


class TransactionDates3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    accptnc_dt_tm: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "AccptncDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    trad_actvty_ctrctl_sttlm_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "TradActvtyCtrctlSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    trad_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    intr_bk_sttlm_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "IntrBkSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    start_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    end_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    tx_dt_tm: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "TxDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    prtry: list[ProprietaryDate3] = field(
        default_factory=list,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class ActiveOrHistoricCurrencyAndAmountRange2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    amt: ImpliedCurrencyAmountRange1Choice = field(
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    cdt_dbt_ind: None | CreditDebitCode = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    ccy: str = field(
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[A-Z]{3,3}",
        }
    )


class BranchData3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: None | str = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: None | str = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: None | PostalAddress24 = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class CardIndividualTransaction2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    iccrltd_data: None | str = field(
        default=None,
        metadata={
            "name": "ICCRltdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 1025,
        },
    )
    pmt_cntxt: None | PaymentContext3 = field(
        default=None,
        metadata={
            "name": "PmtCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    addtl_svc: None | CardPaymentServiceType2Code = field(
        default=None,
        metadata={
            "name": "AddtlSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    tx_ctgy: None | str = field(
        default=None,
        metadata={
            "name": "TxCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    sale_rcncltn_id: None | str = field(
        default=None,
        metadata={
            "name": "SaleRcncltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sale_ref_nb: None | str = field(
        default=None,
        metadata={
            "name": "SaleRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    re_presntmnt_rsn: None | str = field(
        default=None,
        metadata={
            "name": "RePresntmntRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    seq_nb: None | str = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_id: None | TransactionIdentifier1 = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    pdct: None | Product2 = field(
        default=None,
        metadata={
            "name": "Pdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    vldtn_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "VldtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    vldtn_seq_nb: None | str = field(
        default=None,
        metadata={
            "name": "VldtnSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class CashAccount38(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: AccountIdentification4Choice = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    tp: None | CashAccountType2Choice = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    ccy: None | str = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: None | str = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prxy: None | ProxyAccountIdentification1 = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class CreditorReferenceInformation2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tp: None | CreditorReferenceType2 = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    ref: None | str = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


class DocumentLineInformation1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: list[DocumentLineIdentification1] = field(
        default_factory=list,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_occurs": 1,
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    amt: None | RemittanceAmount3 = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class FinancialInstitutionIdentification18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    bicfi: None | str = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: None | ClearingSystemMemberIdentification2 = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    lei: None | str = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: None | str = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: None | PostalAddress24 = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    othr: None | GenericFinancialIdentification1 = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class NameAndAddress16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    nm: str = field(
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 140,
        }
    )
    adr: PostalAddress24 = field(
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )


class Party38Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    org_id: None | OrganisationIdentification29 = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    prvt_id: None | PersonIdentification13 = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class PaymentCard4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    plain_card_data: None | PlainCardData1 = field(
        default=None,
        metadata={
            "name": "PlainCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    card_ctry_cd: None | str = field(
        default=None,
        metadata={
            "name": "CardCtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[0-9]{3}",
        },
    )
    card_brnd: None | GenericIdentification1 = field(
        default=None,
        metadata={
            "name": "CardBrnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    addtl_card_data: None | str = field(
        default=None,
        metadata={
            "name": "AddtlCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )


class PointOfInteraction1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: GenericIdentification32 = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    sys_nm: None | str = field(
        default=None,
        metadata={
            "name": "SysNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    grp_id: None | str = field(
        default=None,
        metadata={
            "name": "GrpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cpblties: None | PointOfInteractionCapabilities1 = field(
        default=None,
        metadata={
            "name": "Cpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    cmpnt: list[PointOfInteractionComponent1] = field(
        default_factory=list,
        metadata={
            "name": "Cmpnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class TaxAmount2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    rate: None | Decimal = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    taxbl_base_amt: None | ActiveOrHistoricCurrencyAndAmount = field(
        default=None,
        metadata={
            "name": "TaxblBaseAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    ttl_amt: None | ActiveOrHistoricCurrencyAndAmount = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    dtls: list[TaxRecordDetails2] = field(
        default_factory=list,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class TotalsPerBankTransactionCode5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    nb_of_ntries: None | str = field(
        default=None,
        metadata={
            "name": "NbOfNtries",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[0-9]{1,15}",
        },
    )
    sum: None | Decimal = field(
        default=None,
        metadata={
            "name": "Sum",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    ttl_net_ntry: None | AmountAndDirection35 = field(
        default=None,
        metadata={
            "name": "TtlNetNtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    cdt_ntries: None | NumberAndSumOfTransactions1 = field(
        default=None,
        metadata={
            "name": "CdtNtries",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    dbt_ntries: None | NumberAndSumOfTransactions1 = field(
        default=None,
        metadata={
            "name": "DbtNtries",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    fcst_ind: None | bool = field(
        default=None,
        metadata={
            "name": "FcstInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    bk_tx_cd: BankTransactionCodeStructure4 = field(
        metadata={
            "name": "BkTxCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    avlbty: list[CashAvailability1] = field(
        default_factory=list,
        metadata={
            "name": "Avlbty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    dt: None | DateAndDateTime2Choice = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class TransactionPrice4Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    deal_pric: None | Price7 = field(
        default=None,
        metadata={
            "name": "DealPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    prtry: list[ProprietaryPrice2] = field(
        default_factory=list,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class BranchAndFinancialInstitutionIdentification6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    fin_instn_id: FinancialInstitutionIdentification18 = field(
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    brnch_id: None | BranchData3 = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class CardEntry4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    card: None | PaymentCard4 = field(
        default=None,
        metadata={
            "name": "Card",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    poi: None | PointOfInteraction1 = field(
        default=None,
        metadata={
            "name": "POI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    aggtd_ntry: None | CardAggregated2 = field(
        default=None,
        metadata={
            "name": "AggtdNtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    pre_pd_acct: None | CashAccount38 = field(
        default=None,
        metadata={
            "name": "PrePdAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class CardTransaction3Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    aggtd: None | CardAggregated2 = field(
        default=None,
        metadata={
            "name": "Aggtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    indv: None | CardIndividualTransaction2 = field(
        default=None,
        metadata={
            "name": "Indv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class PartyIdentification135(BaseModel):
    model_config = ConfigDict(defer_build=True)
    nm: None | str = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: None | PostalAddress24 = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    id: None | Party38Choice = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    ctry_of_res: None | str = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: None | Contact4 = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class Rate4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tp: RateType4Choice = field(
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    vldty_rg: None | ActiveOrHistoricCurrencyAndAmountRange2 = field(
        default=None,
        metadata={
            "name": "VldtyRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class ReferredDocumentInformation7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tp: None | ReferredDocumentType4 = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    nb: None | str = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rltd_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "RltdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    line_dtls: list[DocumentLineInformation1] = field(
        default_factory=list,
        metadata={
            "name": "LineDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class RemittanceLocationData1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    mtd: RemittanceLocationMethod2Code = field(
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    elctrnc_adr: None | str = field(
        default=None,
        metadata={
            "name": "ElctrncAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    pstl_adr: None | NameAndAddress16 = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class TaxRecord2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tp: None | str = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctgy: None | str = field(
        default=None,
        metadata={
            "name": "Ctgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctgy_dtls: None | str = field(
        default=None,
        metadata={
            "name": "CtgyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dbtr_sts: None | str = field(
        default=None,
        metadata={
            "name": "DbtrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cert_id: None | str = field(
        default=None,
        metadata={
            "name": "CertId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    frms_cd: None | str = field(
        default=None,
        metadata={
            "name": "FrmsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prd: None | TaxPeriod2 = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    tax_amt: None | TaxAmount2 = field(
        default=None,
        metadata={
            "name": "TaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    addtl_inf: None | str = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )


class TotalTransactions6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ttl_ntries: None | NumberAndSumOfTransactions4 = field(
        default=None,
        metadata={
            "name": "TtlNtries",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    ttl_cdt_ntries: None | NumberAndSumOfTransactions1 = field(
        default=None,
        metadata={
            "name": "TtlCdtNtries",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    ttl_dbt_ntries: None | NumberAndSumOfTransactions1 = field(
        default=None,
        metadata={
            "name": "TtlDbtNtries",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    ttl_ntries_per_bk_tx_cd: list[TotalsPerBankTransactionCode5] = field(
        default_factory=list,
        metadata={
            "name": "TtlNtriesPerBkTxCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class AccountInterest4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tp: None | InterestType1Choice = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rate: list[Rate4] = field(
        default_factory=list,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    fr_to_dt: None | DateTimePeriod1 = field(
        default=None,
        metadata={
            "name": "FrToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rsn: None | str = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax: None | TaxCharges2 = field(
        default=None,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class CardTransaction17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    card: None | PaymentCard4 = field(
        default=None,
        metadata={
            "name": "Card",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    poi: None | PointOfInteraction1 = field(
        default=None,
        metadata={
            "name": "POI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    tx: None | CardTransaction3Choice = field(
        default=None,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    pre_pd_acct: None | CashAccount38 = field(
        default=None,
        metadata={
            "name": "PrePdAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class CashAccount39(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: AccountIdentification4Choice = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    tp: None | CashAccountType2Choice = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    ccy: None | str = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: None | str = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prxy: None | ProxyAccountIdentification1 = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    ownr: None | PartyIdentification135 = field(
        default=None,
        metadata={
            "name": "Ownr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    svcr: None | BranchAndFinancialInstitutionIdentification6 = field(
        default=None,
        metadata={
            "name": "Svcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class ChargesRecord3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    amt: ActiveOrHistoricCurrencyAndAmount = field(
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    cdt_dbt_ind: None | CreditDebitCode = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    chrg_incl_ind: None | bool = field(
        default=None,
        metadata={
            "name": "ChrgInclInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    tp: None | ChargeType3Choice = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rate: None | Decimal = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    br: None | ChargeBearerType1Code = field(
        default=None,
        metadata={
            "name": "Br",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    agt: None | BranchAndFinancialInstitutionIdentification6 = field(
        default=None,
        metadata={
            "name": "Agt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    tax: None | TaxCharges2 = field(
        default=None,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class Garnishment3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tp: GarnishmentType1 = field(
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    grnshee: None | PartyIdentification135 = field(
        default=None,
        metadata={
            "name": "Grnshee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    grnshmt_admstr: None | PartyIdentification135 = field(
        default=None,
        metadata={
            "name": "GrnshmtAdmstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    ref_nb: None | str = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rmtd_amt: None | ActiveOrHistoricCurrencyAndAmount = field(
        default=None,
        metadata={
            "name": "RmtdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    fmly_mdcl_insrnc_ind: None | bool = field(
        default=None,
        metadata={
            "name": "FmlyMdclInsrncInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    mplyee_termntn_ind: None | bool = field(
        default=None,
        metadata={
            "name": "MplyeeTermntnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class GroupHeader81(BaseModel):
    model_config = ConfigDict(defer_build=True)
    msg_id: str = field(
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    cre_dt_tm: XmlDateTime = field(
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    msg_rcpt: None | PartyIdentification135 = field(
        default=None,
        metadata={
            "name": "MsgRcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    msg_pgntn: None | Pagination1 = field(
        default=None,
        metadata={
            "name": "MsgPgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    orgnl_biz_qry: None | OriginalBusinessQuery1 = field(
        default=None,
        metadata={
            "name": "OrgnlBizQry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    addtl_inf: None | str = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 500,
        },
    )


class InterestRecord2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    amt: ActiveOrHistoricCurrencyAndAmount = field(
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    cdt_dbt_ind: CreditDebitCode = field(
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    tp: None | InterestType1Choice = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rate: None | Rate4 = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    fr_to_dt: None | DateTimePeriod1 = field(
        default=None,
        metadata={
            "name": "FrToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rsn: None | str = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax: None | TaxCharges2 = field(
        default=None,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class Party40Choice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    pty: None | PartyIdentification135 = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    agt: None | BranchAndFinancialInstitutionIdentification6 = field(
        default=None,
        metadata={
            "name": "Agt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class PaymentReturnReason5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    orgnl_bk_tx_cd: None | BankTransactionCodeStructure4 = field(
        default=None,
        metadata={
            "name": "OrgnlBkTxCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    orgtr: None | PartyIdentification135 = field(
        default=None,
        metadata={
            "name": "Orgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rsn: None | ReturnReason5Choice = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 105,
        },
    )


class ProprietaryAgent4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tp: str = field(
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    agt: BranchAndFinancialInstitutionIdentification6 = field(
        metadata={
            "name": "Agt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )


class RemittanceLocation7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    rmt_id: None | str = field(
        default=None,
        metadata={
            "name": "RmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rmt_lctn_dtls: list[RemittanceLocationData1] = field(
        default_factory=list,
        metadata={
            "name": "RmtLctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class TaxInformation7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cdtr: None | TaxParty1 = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    dbtr: None | TaxParty2 = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    ultmt_dbtr: None | TaxParty2 = field(
        default=None,
        metadata={
            "name": "UltmtDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    admstn_zone: None | str = field(
        default=None,
        metadata={
            "name": "AdmstnZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_nb: None | str = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    mtd: None | str = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ttl_taxbl_base_amt: None | ActiveOrHistoricCurrencyAndAmount = field(
        default=None,
        metadata={
            "name": "TtlTaxblBaseAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    ttl_tax_amt: None | ActiveOrHistoricCurrencyAndAmount = field(
        default=None,
        metadata={
            "name": "TtlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    seq_nb: None | Decimal = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcrd: list[TaxRecord2] = field(
        default_factory=list,
        metadata={
            "name": "Rcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class TaxInformation8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cdtr: None | TaxParty1 = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    dbtr: None | TaxParty2 = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    admstn_zone: None | str = field(
        default=None,
        metadata={
            "name": "AdmstnZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_nb: None | str = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    mtd: None | str = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ttl_taxbl_base_amt: None | ActiveOrHistoricCurrencyAndAmount = field(
        default=None,
        metadata={
            "name": "TtlTaxblBaseAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    ttl_tax_amt: None | ActiveOrHistoricCurrencyAndAmount = field(
        default=None,
        metadata={
            "name": "TtlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    seq_nb: None | Decimal = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcrd: list[TaxRecord2] = field(
        default_factory=list,
        metadata={
            "name": "Rcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class Charges6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ttl_chrgs_and_tax_amt: None | ActiveOrHistoricCurrencyAndAmount = field(
        default=None,
        metadata={
            "name": "TtlChrgsAndTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rcrd: list[ChargesRecord3] = field(
        default_factory=list,
        metadata={
            "name": "Rcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class ProprietaryParty5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tp: str = field(
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    pty: Party40Choice = field(
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )


class StructuredRemittanceInformation16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    rfrd_doc_inf: list[ReferredDocumentInformation7] = field(
        default_factory=list,
        metadata={
            "name": "RfrdDocInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rfrd_doc_amt: None | RemittanceAmount2 = field(
        default=None,
        metadata={
            "name": "RfrdDocAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    cdtr_ref_inf: None | CreditorReferenceInformation2 = field(
        default=None,
        metadata={
            "name": "CdtrRefInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    invcr: None | PartyIdentification135 = field(
        default=None,
        metadata={
            "name": "Invcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    invcee: None | PartyIdentification135 = field(
        default=None,
        metadata={
            "name": "Invcee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    tax_rmt: None | TaxInformation7 = field(
        default=None,
        metadata={
            "name": "TaxRmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    grnshmt_rmt: None | Garnishment3 = field(
        default=None,
        metadata={
            "name": "GrnshmtRmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    addtl_rmt_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlRmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "max_occurs": 3,
            "min_length": 1,
            "max_length": 140,
        },
    )


class TransactionAgents5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    instg_agt: None | BranchAndFinancialInstitutionIdentification6 = field(
        default=None,
        metadata={
            "name": "InstgAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    instd_agt: None | BranchAndFinancialInstitutionIdentification6 = field(
        default=None,
        metadata={
            "name": "InstdAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    dbtr_agt: None | BranchAndFinancialInstitutionIdentification6 = field(
        default=None,
        metadata={
            "name": "DbtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    cdtr_agt: None | BranchAndFinancialInstitutionIdentification6 = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    intrmy_agt1: None | BranchAndFinancialInstitutionIdentification6 = field(
        default=None,
        metadata={
            "name": "IntrmyAgt1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    intrmy_agt2: None | BranchAndFinancialInstitutionIdentification6 = field(
        default=None,
        metadata={
            "name": "IntrmyAgt2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    intrmy_agt3: None | BranchAndFinancialInstitutionIdentification6 = field(
        default=None,
        metadata={
            "name": "IntrmyAgt3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rcvg_agt: None | BranchAndFinancialInstitutionIdentification6 = field(
        default=None,
        metadata={
            "name": "RcvgAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    dlvrg_agt: None | BranchAndFinancialInstitutionIdentification6 = field(
        default=None,
        metadata={
            "name": "DlvrgAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    issg_agt: None | BranchAndFinancialInstitutionIdentification6 = field(
        default=None,
        metadata={
            "name": "IssgAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    sttlm_plc: None | BranchAndFinancialInstitutionIdentification6 = field(
        default=None,
        metadata={
            "name": "SttlmPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    prtry: list[ProprietaryAgent4] = field(
        default_factory=list,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class TransactionInterest4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ttl_intrst_and_tax_amt: None | ActiveOrHistoricCurrencyAndAmount = field(
        default=None,
        metadata={
            "name": "TtlIntrstAndTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rcrd: list[InterestRecord2] = field(
        default_factory=list,
        metadata={
            "name": "Rcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class RemittanceInformation16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ustrd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Ustrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    strd: list[StructuredRemittanceInformation16] = field(
        default_factory=list,
        metadata={
            "name": "Strd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class TransactionParties6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    initg_pty: None | Party40Choice = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    dbtr: None | Party40Choice = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    dbtr_acct: None | CashAccount38 = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    ultmt_dbtr: None | Party40Choice = field(
        default=None,
        metadata={
            "name": "UltmtDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    cdtr: None | Party40Choice = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    cdtr_acct: None | CashAccount38 = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    ultmt_cdtr: None | Party40Choice = field(
        default=None,
        metadata={
            "name": "UltmtCdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    tradg_pty: None | Party40Choice = field(
        default=None,
        metadata={
            "name": "TradgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    prtry: list[ProprietaryParty5] = field(
        default_factory=list,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class EntryTransaction10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    refs: None | TransactionReferences6 = field(
        default=None,
        metadata={
            "name": "Refs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    amt: None | ActiveOrHistoricCurrencyAndAmount = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    cdt_dbt_ind: None | CreditDebitCode = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    amt_dtls: None | AmountAndCurrencyExchange3 = field(
        default=None,
        metadata={
            "name": "AmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    avlbty: list[CashAvailability1] = field(
        default_factory=list,
        metadata={
            "name": "Avlbty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    bk_tx_cd: None | BankTransactionCodeStructure4 = field(
        default=None,
        metadata={
            "name": "BkTxCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    chrgs: None | Charges6 = field(
        default=None,
        metadata={
            "name": "Chrgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    intrst: None | TransactionInterest4 = field(
        default=None,
        metadata={
            "name": "Intrst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rltd_pties: None | TransactionParties6 = field(
        default=None,
        metadata={
            "name": "RltdPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rltd_agts: None | TransactionAgents5 = field(
        default=None,
        metadata={
            "name": "RltdAgts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    lcl_instrm: None | LocalInstrument2Choice = field(
        default=None,
        metadata={
            "name": "LclInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    purp: None | Purpose2Choice = field(
        default=None,
        metadata={
            "name": "Purp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rltd_rmt_inf: list[RemittanceLocation7] = field(
        default_factory=list,
        metadata={
            "name": "RltdRmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "max_occurs": 10,
        },
    )
    rmt_inf: None | RemittanceInformation16 = field(
        default=None,
        metadata={
            "name": "RmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rltd_dts: None | TransactionDates3 = field(
        default=None,
        metadata={
            "name": "RltdDts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rltd_pric: None | TransactionPrice4Choice = field(
        default=None,
        metadata={
            "name": "RltdPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rltd_qties: list[TransactionQuantities3Choice] = field(
        default_factory=list,
        metadata={
            "name": "RltdQties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    fin_instrm_id: None | SecurityIdentification19 = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    tax: None | TaxInformation8 = field(
        default=None,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rtr_inf: None | PaymentReturnReason5 = field(
        default=None,
        metadata={
            "name": "RtrInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    corp_actn: None | CorporateAction9 = field(
        default=None,
        metadata={
            "name": "CorpActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    sfkpg_acct: None | SecuritiesAccount19 = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    csh_dpst: list[CashDeposit1] = field(
        default_factory=list,
        metadata={
            "name": "CshDpst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    card_tx: None | CardTransaction17 = field(
        default=None,
        metadata={
            "name": "CardTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    addtl_tx_inf: None | str = field(
        default=None,
        metadata={
            "name": "AddtlTxInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 500,
        },
    )
    splmtry_data: list[SupplementaryData1] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class EntryDetails9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    btch: None | BatchInformation2 = field(
        default=None,
        metadata={
            "name": "Btch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    tx_dtls: list[EntryTransaction10] = field(
        default_factory=list,
        metadata={
            "name": "TxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class ReportEntry10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    ntry_ref: None | str = field(
        default=None,
        metadata={
            "name": "NtryRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: ActiveOrHistoricCurrencyAndAmount = field(
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    cdt_dbt_ind: CreditDebitCode = field(
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    rvsl_ind: None | bool = field(
        default=None,
        metadata={
            "name": "RvslInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    sts: EntryStatus1Choice = field(
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    bookg_dt: None | DateAndDateTime2Choice = field(
        default=None,
        metadata={
            "name": "BookgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    val_dt: None | DateAndDateTime2Choice = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    acct_svcr_ref: None | str = field(
        default=None,
        metadata={
            "name": "AcctSvcrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    avlbty: list[CashAvailability1] = field(
        default_factory=list,
        metadata={
            "name": "Avlbty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    bk_tx_cd: BankTransactionCodeStructure4 = field(
        metadata={
            "name": "BkTxCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    comssn_wvr_ind: None | bool = field(
        default=None,
        metadata={
            "name": "ComssnWvrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    addtl_inf_ind: None | MessageIdentification2 = field(
        default=None,
        metadata={
            "name": "AddtlInfInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    amt_dtls: None | AmountAndCurrencyExchange3 = field(
        default=None,
        metadata={
            "name": "AmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    chrgs: None | Charges6 = field(
        default=None,
        metadata={
            "name": "Chrgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    tech_inpt_chanl: None | TechnicalInputChannel1Choice = field(
        default=None,
        metadata={
            "name": "TechInptChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    intrst: None | TransactionInterest4 = field(
        default=None,
        metadata={
            "name": "Intrst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    card_tx: None | CardEntry4 = field(
        default=None,
        metadata={
            "name": "CardTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    ntry_dtls: list[EntryDetails9] = field(
        default_factory=list,
        metadata={
            "name": "NtryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    addtl_ntry_inf: None | str = field(
        default=None,
        metadata={
            "name": "AddtlNtryInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 500,
        },
    )


class AccountStatement9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 35,
        }
    )
    stmt_pgntn: None | Pagination1 = field(
        default=None,
        metadata={
            "name": "StmtPgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    elctrnc_seq_nb: None | Decimal = field(
        default=None,
        metadata={
            "name": "ElctrncSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rptg_seq: None | SequenceRange1Choice = field(
        default=None,
        metadata={
            "name": "RptgSeq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    lgl_seq_nb: None | Decimal = field(
        default=None,
        metadata={
            "name": "LglSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    cre_dt_tm: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    fr_to_dt: None | DateTimePeriod1 = field(
        default=None,
        metadata={
            "name": "FrToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    cpy_dplct_ind: None | CopyDuplicate1Code = field(
        default=None,
        metadata={
            "name": "CpyDplctInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    rptg_src: None | ReportingSource1Choice = field(
        default=None,
        metadata={
            "name": "RptgSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    acct: CashAccount39 = field(
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    rltd_acct: None | CashAccount38 = field(
        default=None,
        metadata={
            "name": "RltdAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    intrst: list[AccountInterest4] = field(
        default_factory=list,
        metadata={
            "name": "Intrst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    bal: list[CashBalance8] = field(
        default_factory=list,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_occurs": 1,
        },
    )
    txs_summry: None | TotalTransactions6 = field(
        default=None,
        metadata={
            "name": "TxsSummry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    ntry: list[ReportEntry10] = field(
        default_factory=list,
        metadata={
            "name": "Ntry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )
    addtl_stmt_inf: None | str = field(
        default=None,
        metadata={
            "name": "AddtlStmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_length": 1,
            "max_length": 500,
        },
    )


class BankToCustomerStatementV08(BaseModel):
    model_config = ConfigDict(defer_build=True)
    grp_hdr: GroupHeader81 = field(
        metadata={
            "name": "GrpHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        }
    )
    stmt: list[AccountStatement9] = field(
        default_factory=list,
        metadata={
            "name": "Stmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08",
        },
    )


class Document(BaseModel):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08"

    model_config = ConfigDict(defer_build=True)
    bk_to_cstmr_stmt: BankToCustomerStatementV08 = field(
        metadata={
            "name": "BkToCstmrStmt",
            "type": "Element",
        }
    )
