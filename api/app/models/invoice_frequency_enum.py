import enum


class InvoiceFrequencyEnum(enum.Enum):

    weekly = "weekly"
    biweekly = "biweekly"
    monthly = "monthly"
    one_time = "one-time"
    adhoc = "adhoc"
