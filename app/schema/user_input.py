from pydantic import BaseModel, Field, field_validator
from typing import Literal, Annotated


'tenure','MonthlyCharges','TotalCharges'
'tenure_group','Contract','InternetService','PaymentMethod','OnlineBackup'

# Internet Serice - DSL, Fiber Optic, No
# Online Backup - Yes, No,  No InternetService
# Contract - Month-to-Month ,One Year Contract, Two Year Contract
# PaymentMethod - Electronic check, Malid Check,Bank Transfer (automatic), Credit Card(automatic)


class UserInput(BaseModel):
    tenure: Annotated[int, Field(..., gt=0)]
    Contract: Annotated[Literal['Month-to-Month','One Year Contract','Two Year Contract'], Field(...)]
    InternetService: Annotated[Literal['DSL', 'Fiber Optic', 'No'], Field(...)]
    PaymentMethod: Annotated[Literal['Electronic check', 'Malid Check','Bank Transfer (automatic)', 'Credit Card(automatic)'], Field(...)]
    MonthlyCharges:Annotated[float,Field(...)]
    TotalCharges:Annotated[float,Field(...)]
    OnlineBackup: Annotated[Literal['Yes', 'No','No InternetService'], Field(...)]
