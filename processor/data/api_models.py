from datetime import datetime
import typing
from dataclasses import dataclass
from pydantic import BaseModel, Field


class HeaderMessage(BaseModel):
    ID:  str = Field(alias="message:ID")
    Test: bool = Field(alias="message:Test")
    Prepared: datetime= Field(alias="message:Prepared")
    Sender: typing.Dict = Field(alias="message:Sender")


class HeaderDataStructure(BaseModel):
    structureID: str = Field(alias="@structureID")
    dimensionAtObservation: str = Field(alias="@dimensionAtObservation")
    Structure: typing.Dict = Field(alias="common:Structure")

@dataclass
class genericValue():
    id: str
    value: str

class genericAtributes(BaseModel):
    Attributes: genericValue

class genericObsValue(BaseModel):
    value: str

class genericObsDimension(BaseModel):
    value: str

class genericObs(BaseModel): #list
    ObsDimension: genericObsDimension
    ObsValue: genericObsValue
    Attributes: genericAtributes


class genericSeriesKey(BaseModel):
    value: typing.List[genericValue]


class genericSeries(BaseModel):
    series: genericSeriesKey
    attribtes: genericAtributes
    obs: typing.List[genericObs]

class MessageDataSet(BaseModel):
    action: str = Field(alias="@action")
    validFromDate:datetime = Field(alias="@validFromDate")
    structureRef: str = Field(alias="@structureRef")
    series: genericSeries


@dataclass
class GenericData(BaseModel):

    message :str = Field(alias="@xmlns:message")
    common: str = Field(alias="@xmlns:common")
    xsi: str = Field(alias="@xmlns:xsi")
    generic: str = Field(alias="@xmlns:generic")
    schemaLocation: str = Field(alias="@xsi:schemaLocation")
    # Header: typing.Dict[HeaderMessage, HeaderDataStructure]
    # DataSet: MessageDataSet


    def __init__(self, **kwargs):
        return super().__init__(**kwargs)







