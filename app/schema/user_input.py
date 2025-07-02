from pydantic import BaseModel, Field, field_validator
from typing import Literal, Annotated


'tenure','MonthlyCharges','TotalCharges'
'tenure_group','Contract','InternetService','PaymentMethod','OnlineBackup'

# Internet Serice - DSL, Fiber optic, No
# Online Backup - Yes, No, No InternetService
# Contract - Month-to-month ,One year Contract, Two year
# PaymentMethod - Electronic check, Malid check,Bank transfer (automatic), Credit card(automatic)


class UserInput(BaseModel):
    tenure: Annotated[int, Field(..., gt=0)]
    Contract: Annotated[Literal['Month-to-month','One year Contract','Two year'], Field(...)]
    InternetService: Annotated[Literal['DSL', 'Fiber optic', 'No'], Field(...)]
    PaymentMethod: Annotated[Literal['Electronic check', 'Malid check','Bank transfer (automatic)', 'Credit card (automatic)'], Field(...)]
    MonthlyCharges:Annotated[float,Field(...)]
    TotalCharges:Annotated[float,Field(...)]
    OnlineBackup: Annotated[Literal['Yes', 'No','No InternetService'], Field(...)]


