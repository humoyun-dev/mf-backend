from infobip_api_client.api_client import ApiClient, Configuration
from infobip_api_client.model.sms_advanced_textual_request import SmsAdvancedTextualRequest
from infobip_api_client.model.sms_destination import SmsDestination
from infobip_api_client.model.sms_response import SmsResponse
from infobip_api_client.model.sms_textual_message import SmsTextualMessage
from infobip_api_client.api.send_sms_api import SendSmsApi
from infobip_api_client.exceptions import ApiException


def send_sms_verification(phone_number, verification_code):

    BASE_URL = "j3mry9.api.infobip.com"
    API_KEY = "9435f1315e4a4c0343a59bbe9e72ea74-253ca2a4-d46f-458b-a6cc-48735d306875"

    SENDER = "MF-HALAL"
    MESSAGE_TEXT = f"Tasdiqlash kodi: {verification_code} \n Код подтверждения: {verification_code}"


    client_config = Configuration(
        host=BASE_URL,
        api_key={"APIKeyHeader": API_KEY},
        api_key_prefix={"APIKeyHeader": "App"},
    )

    api_client = ApiClient(client_config)


    sms_request = SmsAdvancedTextualRequest(
        messages=[
            SmsTextualMessage(
                destinations=[
                    SmsDestination(
                        to=phone_number,
                    ),
                ],
                _from=SENDER,
                text=MESSAGE_TEXT,
            )
        ]
    )


    api_instance = SendSmsApi(api_client)

    try:
        api_response: SmsResponse = api_instance.send_sms_message(sms_advanced_textual_request=sms_request)
        print(api_response)
    except ApiException as ex:
        print("Error occurred while trying to send SMS message.")
        print(ex)
