from ast import alias
from datetime import datetime
import typing
from dataclasses import dataclass
from pydantic import BaseModel, Field


class HeaderMessage(BaseModel):
    ID:  str = Field(alias="message:ID")
    Test: bool = Field(alias="message:Test")
    Prepared: datetime= Field(alias="message:Prepared")
    Sender: typing.Dict = Field(alias="message:Sender")
    Structure:  typing.Dict = Field(alias="message:Structure")


class HeaderDataStructure(BaseModel):
    structureID: str = Field(alias="@structureID")
    dimensionAtObservation: str = Field(alias="@dimensionAtObservation")
    Structure: typing.Dict = Field(alias="common:Structure")

@dataclass
class genericValue():
    id: str = Field(alias="@id")
    value: str = Field(alias="@value")

class genericAtributes(BaseModel):
    Attributes: genericValue = Field(alias="generic:Attributes")

class genericObsValue(BaseModel):
    value: str =  Field(alias="@value")

class genericObsDimension(BaseModel):
   value: str =  Field(alias="@value")

class genericObs(BaseModel):
    ObsDimension: genericObsDimension = Field(alias="generic:ObsDimension")
    ObsValue: genericObsValue = Field(alias="generic:ObsValue")
    Attributes: genericAtributes = Field(alias="generic:Attributes")


class genericSeriesKey(BaseModel):
    value: typing.List[genericValue] = Field(alias="generic:Value")


class genericSeries(BaseModel):
    series_key: typing.Dict = Field(alias="generic:SeriesKey")
    attributes: typing.Dict = Field(alias="generic:Attributes")
    series: typing.Dict = Field(alias="generic:Series")

class MessageDataSet(BaseModel):
    action: str = Field(alias="@action")
    validFromDate:datetime = Field(alias="@validFromDate")
    structureRef: str = Field(alias="@structureRef")
    series: typing.Dict = Field(alias="generic:Series")


class FileRequestData(BaseModel):
    date:str
    country: str
    purchase: float
    currency = str
    net = float
    Vat = float


@dataclass
class GenericData(BaseModel):

    message :str = Field(alias="@xmlns:message")
    common: str = Field(alias="@xmlns:common")
    xsi: str = Field(alias="@xmlns:xsi")
    generic: str = Field(alias="@xmlns:generic")
    schemaLocation: str = Field(alias="@xsi:schemaLocation")
    header: HeaderMessage = Field(alias="message:Header")
    dataSet: MessageDataSet = Field(alias="message:DataSet")


    def __init__(self, **kwargs):
        return super().__init__(**kwargs)







