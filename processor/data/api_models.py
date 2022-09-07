from datetime import datetime
import typing
from dataclasses import dataclass
from pydantic import BaseModel, Field


class HeaderMessage(BaseModel):
    """Models the message header object."""

    ID:  str = Field(alias="message:ID")
    Test: str = Field(alias="message:Test")
    Prepared: datetime= Field(alias="message:Prepared")
    Sender: typing.Dict = Field(alias="message:Sender")
    Structure:  typing.Dict = Field(alias="message:Structure")

class HeaderDataStructure(BaseModel):
    """Models the  data structure header object. """
    structureID: str = Field(alias="@structureID")
    dimensionAtObservation: str = Field(alias="@dimensionAtObservation")
    Structure: typing.Dict = Field(alias="common:Structure")

@dataclass
class genericValue():
    """Models the  generic value object. """

    id: str = Field(alias="@id")
    value: str = Field(alias="@value")

class genericAtributes(BaseModel):
    """Models the generic attributes object."""

    Attributes: genericValue = Field(alias="generic:Attributes")

class genericObsValue(BaseModel):
    """models the generic obs value object."""

    value: str =  Field(alias="@value")

class genericObsDimension(BaseModel):
    """Models the generic obs dimesion object"""

    value: str =  Field(alias="@value")

class genericObs(BaseModel):
    """Models the generic series object"""

    ObsDimension: genericObsDimension = Field(alias="generic:ObsDimension")
    ObsValue: genericObsValue = Field(alias="generic:ObsValue")
    Attributes: genericAtributes = Field(alias="generic:Attributes")


class genericSeriesKey(BaseModel):
    """Models the generic series key object"""

    value: typing.List[genericValue] = Field(alias="generic:Value")

class genericSeries(BaseModel):
    """Models the generic series object"""

    series_key: genericSeriesKey = Field(alias="generic:SeriesKey")
    attributes: genericAtributes = Field(alias="generic:Attributes")
    series: typing.List[genericObs] = Field(alias="generic:Series")

class MessageDataSet(BaseModel):
    """Models the data set object"""

    action: str = Field(alias="@action")
    validFromDate:datetime = Field(alias="@validFromDate")
    structureRef: str = Field(alias="@structureRef")
    series: typing.Dict = Field(alias="generic:Series")

class FileRequestData(BaseModel):
    """Models the file request data"""

    date:str
    country: str
    purchase: float
    currency = str
    net = float
    Vat = float

@dataclass
class GenericData(BaseModel):
    """Models the generic data object"""

    message :str = Field(alias="@xmlns:message")
    common: str = Field(alias="@xmlns:common")
    xsi: str = Field(alias="@xmlns:xsi")
    generic: str = Field(alias="@xmlns:generic")
    schemaLocation: str = Field(alias="@xsi:schemaLocation")
    header: HeaderMessage = Field(alias="message:Header")
    dataSet: MessageDataSet = Field(alias="message:DataSet")


    def __init__(self, **kwargs):
        return super().__init__(**kwargs)







