# Color
DARK_BLUE = '#0D0C13'
TEXT_COLOR_LIGHT = '#C4C4C4'
TEXT_COLOR_DARK = '#000'
GRAY_ACCENT = '#5C5C5C'

# Elements
BORDER = "border-width: 2px; border-color: " + GRAY_ACCENT + "; border-style: solid; background: none;"

# Status
STATUS_IDLE = "Waiting for patient data..."
STATUS_READY = "Data loaded"
STATUS_PROCESSING = "Analysing..."
STATUS_DONE = "Done"

# Message
message = dict(
    HEALTHY="Not found typical symptoms of heart disease",
    INCONCLUSIVE="Patient needs further tests to rule out the heart disease",
    SICK="High chance of heart disease"
)

PARAMETERS = ["name", "age", "sex",	"cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]

MODEL = "data/rfc10_3_no_randomness.bin"
