from .rpcbaseerrors import RPCError, AuthKeyError, BadRequestError, FloodError, ForbiddenError, InvalidDCError, ServerError, UnauthorizedError


class RPCErrorNeg503(RPCError):
    code = -503


class AboutTooLongError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided bio is too long' + self._fmt_request(request))


class AccessTokenExpiredError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Bot token expired' + self._fmt_request(request))


class AccessTokenInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided token is not valid' + self._fmt_request(request))


class ActiveUserRequiredError(UnauthorizedError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The method is only available to already activated users' + self._fmt_request(request))


class AdminsTooMuchError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Too many admins' + self._fmt_request(request))


class ApiIdInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The api_id/api_hash combination is invalid' + self._fmt_request(request))


class ApiIdPublishedFloodError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("This API id was published somewhere, you can't use it now" + self._fmt_request(request))


class ArticleTitleEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The title of the article is empty' + self._fmt_request(request))


class AuthBytesInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided authorization is invalid' + self._fmt_request(request))


class AuthKeyDuplicatedError(AuthKeyError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The authorization key (session file) was used under two different IP addresses simultaneously, and can no longer be used. Use the same session exclusively, or use different sessions' + self._fmt_request(request))


class AuthKeyInvalidError(UnauthorizedError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The key is invalid' + self._fmt_request(request))


class AuthKeyPermEmptyError(UnauthorizedError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The method is unavailable for temporary authorization key, not bound to permanent' + self._fmt_request(request))


class AuthKeyUnregisteredError(UnauthorizedError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The key is not registered in the system' + self._fmt_request(request))


class AuthRestartError(ServerError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Restart the authorization process' + self._fmt_request(request))


class BannedRightsInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('You cannot use that set of permissions in this request, i.e. restricting view_messages as a default' + self._fmt_request(request))


class BotsTooMuchError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('There are too many bots in this chat/channel' + self._fmt_request(request))


class BotChannelsNaError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("Bots can't edit admin privileges" + self._fmt_request(request))


class BotGroupsBlockedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("This bot can't be added to groups" + self._fmt_request(request))


class BotInlineDisabledError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("This bot can't be used in inline mode" + self._fmt_request(request))


class BotInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('This is not a valid bot' + self._fmt_request(request))


class BotMethodInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The API access for bot users is restricted. The method you tried to invoke cannot be executed as a bot' + self._fmt_request(request))


class BotMissingError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('This method can only be run by a bot' + self._fmt_request(request))


class BotPollsDisabledError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('You cannot create polls under a bot account' + self._fmt_request(request))


class ButtonDataInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided button data is invalid' + self._fmt_request(request))


class ButtonTypeInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The type of one of the buttons you provided is invalid' + self._fmt_request(request))


class ButtonUrlInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Button URL invalid' + self._fmt_request(request))


class CallAlreadyAcceptedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The call was already accepted' + self._fmt_request(request))


class CallAlreadyDeclinedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The call was already declined' + self._fmt_request(request))


class CallOccupyFailedError(ServerError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The call failed because the user is already making another call' + self._fmt_request(request))


class CallPeerInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided call peer object is invalid' + self._fmt_request(request))


class CallProtocolFlagsInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Call protocol flags invalid' + self._fmt_request(request))


class CdnMethodInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('This method cannot be invoked on a CDN server. Refer to https://core.telegram.org/cdn#schema for available methods' + self._fmt_request(request))


class ChannelsAdminPublicTooMuchError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("You're admin of too many public channels, make some channels private to change the username of this channel" + self._fmt_request(request))


class ChannelsTooMuchError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('You have joined too many channels/supergroups' + self._fmt_request(request))


class ChannelInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Invalid channel object. Make sure to pass the right types, for instance making sure that the request is designed for channels or otherwise look for a different one more suited' + self._fmt_request(request))


class ChannelPrivateError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The channel specified is private and you lack permission to access it. Another reason may be that you were banned from it' + self._fmt_request(request))


class ChannelPublicGroupNaError(ForbiddenError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('channel/supergroup not available' + self._fmt_request(request))


class ChatAboutNotModifiedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('About text has not changed' + self._fmt_request(request))


class ChatAboutTooLongError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Chat about too long' + self._fmt_request(request))


class ChatAdminInviteRequiredError(ForbiddenError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('You do not have the rights to do this' + self._fmt_request(request))


class ChatAdminRequiredError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Chat admin privileges are required to do that in the specified chat (for example, to send a message in a channel which is not yours), or invalid permissions used for the channel or group' + self._fmt_request(request))


class ChatForbiddenError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('You cannot write in this chat' + self._fmt_request(request))


class ChatIdEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided chat ID is empty' + self._fmt_request(request))


class ChatIdInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Invalid object ID for a chat. Make sure to pass the right types, for instance making sure that the request is designed for chats (not channels/megagroups) or otherwise look for a different one more suited\\nAn example working with a megagroup and AddChatUserRequest, it will fail because megagroups are channels. Use InviteToChannelRequest instead' + self._fmt_request(request))


class ChatInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The chat is invalid for this request' + self._fmt_request(request))


class ChatNotModifiedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("The chat or channel wasn't modified (title, invites, username, admins, etc. are the same)" + self._fmt_request(request))


class ChatRestrictedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The chat is restricted and cannot be used in that request' + self._fmt_request(request))


class ChatSendGifsForbiddenError(ForbiddenError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("You can't send gifs in this chat" + self._fmt_request(request))


class ChatSendMediaForbiddenError(ForbiddenError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("You can't send media in this chat" + self._fmt_request(request))


class ChatSendStickersForbiddenError(ForbiddenError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("You can't send stickers in this chat." + self._fmt_request(request))


class ChatTitleEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('No chat title provided' + self._fmt_request(request))


class ChatWriteForbiddenError(ForbiddenError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("You can't write in this chat" + self._fmt_request(request))


class CodeEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided code is empty' + self._fmt_request(request))


class CodeHashInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Code hash invalid' + self._fmt_request(request))


class CodeInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Code invalid (i.e. from email)' + self._fmt_request(request))


class ConnectionApiIdInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided API id is invalid' + self._fmt_request(request))


class ConnectionDeviceModelEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Device model empty' + self._fmt_request(request))


class ConnectionLangPackInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The specified language pack is not valid. This is meant to be used by official applications only so far, leave it empty' + self._fmt_request(request))


class ConnectionLayerInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The very first request must always be InvokeWithLayerRequest' + self._fmt_request(request))


class ConnectionNotInitedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Connection not initialized' + self._fmt_request(request))


class ConnectionSystemEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Connection system empty' + self._fmt_request(request))


class ContactIdInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided contact ID is invalid' + self._fmt_request(request))


class DataInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Encrypted data invalid' + self._fmt_request(request))


class DataJsonInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided JSON data is invalid' + self._fmt_request(request))


class DateEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Date empty' + self._fmt_request(request))


class DcIdInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('This occurs when an authorization is tried to be exported for the same data center one is currently connected to' + self._fmt_request(request))


class DhGAInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('g_a invalid' + self._fmt_request(request))


class EmailHashExpiredError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The email hash expired and cannot be used to verify it' + self._fmt_request(request))


class EmailUnconfirmedError(BadRequestError):
    def __init__(self, request, **kwargs):
        self.code_length = int(kwargs.get('capture', 0))
        super(Exception, self).__init__('Email unconfirmed, the length of the code must be {code_length}'.format(code_length=self.code_length) + self._fmt_request(request))


class EncryptedMessageInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Encrypted message invalid' + self._fmt_request(request))


class EncryptionAlreadyAcceptedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Secret chat already accepted' + self._fmt_request(request))


class EncryptionAlreadyDeclinedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The secret chat was already declined' + self._fmt_request(request))


class EncryptionDeclinedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The secret chat was declined' + self._fmt_request(request))


class EncryptionIdInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided secret chat ID is invalid' + self._fmt_request(request))


class EncryptionOccupyFailedError(ServerError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Internal server error while accepting secret chat' + self._fmt_request(request))


class EntityMentionUserInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("You can't use this entity" + self._fmt_request(request))


class ErrorTextEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided error message is empty' + self._fmt_request(request))


class ExportCardInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Provided card is invalid' + self._fmt_request(request))


class ExternalUrlInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('External URL invalid' + self._fmt_request(request))


class FieldNameEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The field with the name FIELD_NAME is missing' + self._fmt_request(request))


class FieldNameInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The field with the name FIELD_NAME is invalid' + self._fmt_request(request))


class FileIdInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided file id is invalid' + self._fmt_request(request))


class FileMigrateError(InvalidDCError):
    def __init__(self, request, **kwargs):
        self.new_dc = int(kwargs.get('capture', 0))
        super(Exception, self).__init__('The file to be accessed is currently stored in DC {new_dc}'.format(new_dc=self.new_dc) + self._fmt_request(request))


class FilePartsInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The number of file parts is invalid' + self._fmt_request(request))


class FilePart0MissingError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('File part 0 missing' + self._fmt_request(request))


class FilePartEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided file part is empty' + self._fmt_request(request))


class FilePartInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The file part number is invalid' + self._fmt_request(request))


class FilePartLengthInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The length of a file part is invalid' + self._fmt_request(request))


class FilePartSizeInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided file part size is invalid' + self._fmt_request(request))


class FilePartMissingError(BadRequestError):
    def __init__(self, request, **kwargs):
        self.which = int(kwargs.get('capture', 0))
        super(Exception, self).__init__('Part {which} of the file is missing from storage'.format(which=self.which) + self._fmt_request(request))


class FilerefUpgradeNeededError(AuthKeyError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The file reference needs to be refreshed before being used again' + self._fmt_request(request))


class FirstNameInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The first name is invalid' + self._fmt_request(request))


class FloodTestPhoneWaitError(FloodError):
    def __init__(self, request, **kwargs):
        self.seconds = int(kwargs.get('capture', 0))
        super(Exception, self).__init__('A wait of {seconds} seconds is required in the test servers'.format(seconds=self.seconds) + self._fmt_request(request))


class FloodWaitError(FloodError):
    def __init__(self, request, **kwargs):
        self.seconds = int(kwargs.get('capture', 0))
        super(Exception, self).__init__('A wait of {seconds} seconds is required'.format(seconds=self.seconds) + self._fmt_request(request))


class GifIdInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided GIF ID is invalid' + self._fmt_request(request))


class GroupedMediaInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Invalid grouped media' + self._fmt_request(request))


class HashInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided hash is invalid' + self._fmt_request(request))


class HistoryGetFailedError(ServerError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Fetching of history failed' + self._fmt_request(request))


class ImageProcessFailedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Failure while processing image' + self._fmt_request(request))


class InlineResultExpiredError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The inline query expired' + self._fmt_request(request))


class InputConstructorInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided constructor is invalid' + self._fmt_request(request))


class InputFetchErrorError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('An error occurred while deserializing TL parameters' + self._fmt_request(request))


class InputFetchFailError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Failed deserializing TL payload' + self._fmt_request(request))


class InputLayerInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided layer is invalid' + self._fmt_request(request))


class InputMethodInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The invoked method does not exist anymore or has never existed' + self._fmt_request(request))


class InputRequestTooLongError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The input request was too long. This may be a bug in the library as it can occur when serializing more bytes than it should (like appending the vector constructor code at the end of a message)' + self._fmt_request(request))


class InputUserDeactivatedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The specified user was deleted' + self._fmt_request(request))


class InterdcCallErrorError(BadRequestError):
    def __init__(self, request, **kwargs):
        self.dc = int(kwargs.get('capture', 0))
        super(Exception, self).__init__('An error occurred while communicating with DC {dc}'.format(dc=self.dc) + self._fmt_request(request))


class InterdcCallRichErrorError(BadRequestError):
    def __init__(self, request, **kwargs):
        self.dc = int(kwargs.get('capture', 0))
        super(Exception, self).__init__('A rich error occurred while communicating with DC {dc}'.format(dc=self.dc) + self._fmt_request(request))


class InviteHashEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The invite hash is empty' + self._fmt_request(request))


class InviteHashExpiredError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The chat the user tried to join has expired and is not valid anymore' + self._fmt_request(request))


class InviteHashInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The invite hash is invalid' + self._fmt_request(request))


class LangPackInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided language pack is invalid' + self._fmt_request(request))


class LastnameInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The last name is invalid' + self._fmt_request(request))


class LimitInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('An invalid limit was provided. See https://core.telegram.org/api/files#downloading-files' + self._fmt_request(request))


class LocationInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The location given for a file was invalid. See https://core.telegram.org/api/files#downloading-files' + self._fmt_request(request))


class MaxIdInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided max ID is invalid' + self._fmt_request(request))


class Md5ChecksumInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The MD5 check-sums do not match' + self._fmt_request(request))


class MediaCaptionTooLongError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The caption is too long' + self._fmt_request(request))


class MediaEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided media object is invalid' + self._fmt_request(request))


class MediaInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Media invalid' + self._fmt_request(request))


class MediaNewInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The new media to edit the message with is invalid (such as stickers or voice notes)' + self._fmt_request(request))


class MediaPrevInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The old media cannot be edited with anything else (such as stickers or voice notes)' + self._fmt_request(request))


class MemberNoLocationError(ServerError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("An internal failure occurred while fetching user info (couldn't find location)" + self._fmt_request(request))


class MemberOccupyPrimaryLocFailedError(ServerError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Occupation of primary member location failed' + self._fmt_request(request))


class MessageAuthorRequiredError(ForbiddenError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Message author required' + self._fmt_request(request))


class MessageDeleteForbiddenError(ForbiddenError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("You can't delete one of the messages you tried to delete, most likely because it is a service message." + self._fmt_request(request))


class MessageEditTimeExpiredError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("You can't edit this message anymore, too much time has passed since its creation." + self._fmt_request(request))


class MessageEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Empty or invalid UTF-8 message was sent' + self._fmt_request(request))


class MessageIdsEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('No message ids were provided' + self._fmt_request(request))


class MessageIdInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The specified message ID is invalid' + self._fmt_request(request))


class MessageNotModifiedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Content of the message was not modified' + self._fmt_request(request))


class MessageTooLongError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Message was too long. Current maximum length is 4096 UTF-8 characters' + self._fmt_request(request))


class MsgWaitFailedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('A waiting call returned an error' + self._fmt_request(request))


class NeedChatInvalidError(ServerError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided chat is invalid' + self._fmt_request(request))


class NeedMemberInvalidError(ServerError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided member is invalid' + self._fmt_request(request))


class NetworkMigrateError(InvalidDCError):
    def __init__(self, request, **kwargs):
        self.new_dc = int(kwargs.get('capture', 0))
        super(Exception, self).__init__('The source IP address is associated with DC {new_dc}'.format(new_dc=self.new_dc) + self._fmt_request(request))


class NewSaltInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The new salt is invalid' + self._fmt_request(request))


class NewSettingsInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The new settings are invalid' + self._fmt_request(request))


class OffsetInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The given offset was invalid, it must be divisible by 1KB. See https://core.telegram.org/api/files#downloading-files' + self._fmt_request(request))


class OffsetPeerIdInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided offset peer is invalid' + self._fmt_request(request))


class OptionsTooMuchError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('You defined too many options for the poll' + self._fmt_request(request))


class PackShortNameInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Invalid sticker pack name. It must begin with a letter, can\'t contain consecutive underscores and must end in "_by_<bot username>".' + self._fmt_request(request))


class PackShortNameOccupiedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('A stickerpack with this name already exists' + self._fmt_request(request))


class ParticipantsTooFewError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Not enough participants' + self._fmt_request(request))


class ParticipantCallFailedError(ServerError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Failure while making call' + self._fmt_request(request))


class ParticipantVersionOutdatedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The other participant does not use an up to date telegram client with support for calls' + self._fmt_request(request))


class PasswordEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided password is empty' + self._fmt_request(request))


class PasswordHashInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The password (and thus its hash value) you entered is invalid' + self._fmt_request(request))


class PeerFloodError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Too many requests' + self._fmt_request(request))


class PeerIdInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('An invalid Peer was used. Make sure to pass the right peer type' + self._fmt_request(request))


class PeerIdNotSupportedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided peer ID is not supported' + self._fmt_request(request))


class PersistentTimestampEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Persistent timestamp empty' + self._fmt_request(request))


class PersistentTimestampInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Persistent timestamp invalid' + self._fmt_request(request))


class PersistentTimestampOutdatedError(ServerError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Persistent timestamp outdated' + self._fmt_request(request))


class PhoneCodeEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The phone code is missing' + self._fmt_request(request))


class PhoneCodeExpiredError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The confirmation code has expired' + self._fmt_request(request))


class PhoneCodeHashEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The phone code hash is missing' + self._fmt_request(request))


class PhoneCodeInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The phone code entered was invalid' + self._fmt_request(request))


class PhoneMigrateError(InvalidDCError):
    def __init__(self, request, **kwargs):
        self.new_dc = int(kwargs.get('capture', 0))
        super(Exception, self).__init__('The phone number a user is trying to use for authorization is associated with DC {new_dc}'.format(new_dc=self.new_dc) + self._fmt_request(request))


class PhoneNumberAppSignupForbiddenError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('' + self._fmt_request(request))


class PhoneNumberBannedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The used phone number has been banned from Telegram and cannot be used anymore. Maybe check https://www.telegram.org/faq_spam' + self._fmt_request(request))


class PhoneNumberFloodError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('You asked for the code too many times.' + self._fmt_request(request))


class PhoneNumberInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The phone number is invalid' + self._fmt_request(request))


class PhoneNumberOccupiedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The phone number is already in use' + self._fmt_request(request))


class PhoneNumberUnoccupiedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The phone number is not yet being used' + self._fmt_request(request))


class PhonePasswordFloodError(AuthKeyError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('You have tried logging in too many times' + self._fmt_request(request))


class PhonePasswordProtectedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('This phone is password protected' + self._fmt_request(request))


class PhotoContentUrlEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The content from the URL used as a photo appears to be empty or has caused another HTTP error' + self._fmt_request(request))


class PhotoCropSizeSmallError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Photo is too small' + self._fmt_request(request))


class PhotoExtInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The extension of the photo is invalid' + self._fmt_request(request))


class PhotoInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Photo invalid' + self._fmt_request(request))


class PhotoInvalidDimensionsError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The photo dimensions are invalid' + self._fmt_request(request))


class PhotoSaveFileInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The photo you tried to send cannot be saved by Telegram. A reason may be that it exceeds 10MB. Try resizing it locally' + self._fmt_request(request))


class PhotoThumbUrlEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The URL used as a thumbnail appears to be empty or has caused another HTTP error' + self._fmt_request(request))


class PinRestrictedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("You can't pin messages in private chats with other people" + self._fmt_request(request))


class PrivacyKeyInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The privacy key is invalid' + self._fmt_request(request))


class PtsChangeEmptyError(ServerError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('No PTS change' + self._fmt_request(request))


class QueryIdEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The query ID is empty' + self._fmt_request(request))


class QueryIdInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The query ID is invalid' + self._fmt_request(request))


class QueryTooShortError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The query string is too short' + self._fmt_request(request))


class RandomIdDuplicateError(ServerError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('You provided a random ID that was already used' + self._fmt_request(request))


class RandomIdInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('A provided random ID is invalid' + self._fmt_request(request))


class RandomLengthInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Random length invalid' + self._fmt_request(request))


class RangesInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Invalid range provided' + self._fmt_request(request))


class RegIdGenerateFailedError(ServerError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Failure while generating registration ID' + self._fmt_request(request))


class ReplyMarkupInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided reply markup is invalid' + self._fmt_request(request))


class ReplyMarkupTooLongError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The data embedded in the reply markup buttons was too much' + self._fmt_request(request))


class ResultTypeInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Result type invalid' + self._fmt_request(request))


class RightForbiddenError(ForbiddenError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Your admin rights do not allow you to do this' + self._fmt_request(request))


class RpcCallFailError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Telegram is having internal issues, please try again later.' + self._fmt_request(request))


class RpcMcgetFailError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Telegram is having internal issues, please try again later.' + self._fmt_request(request))


class RsaDecryptFailedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Internal RSA decryption failed' + self._fmt_request(request))


class SearchQueryEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The search query is empty' + self._fmt_request(request))


class SendMessageMediaInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The message media was invalid or not specified' + self._fmt_request(request))


class SendMessageTypeInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The message type is invalid' + self._fmt_request(request))


class SessionExpiredError(UnauthorizedError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The authorization has expired' + self._fmt_request(request))


class SessionPasswordNeededError(UnauthorizedError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Two-steps verification is enabled and a password is required' + self._fmt_request(request))


class SessionRevokedError(UnauthorizedError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The authorization has been invalidated, because of the user terminating all sessions' + self._fmt_request(request))


class Sha256HashInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided SHA256 hash is invalid' + self._fmt_request(request))


class ShortnameOccupyFailedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('An error occurred when trying to register the short-name used for the sticker pack. Try a different name' + self._fmt_request(request))


class StartParamEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The start parameter is empty' + self._fmt_request(request))


class StartParamInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Start parameter invalid' + self._fmt_request(request))


class StickersetInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided sticker set is invalid' + self._fmt_request(request))


class StickersEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('No sticker provided' + self._fmt_request(request))


class StickerEmojiInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Sticker emoji invalid' + self._fmt_request(request))


class StickerFileInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Sticker file invalid' + self._fmt_request(request))


class StickerIdInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided sticker ID is invalid' + self._fmt_request(request))


class StickerInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided sticker is invalid' + self._fmt_request(request))


class StickerPngDimensionsError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Sticker png dimensions invalid' + self._fmt_request(request))


class StorageCheckFailedError(ServerError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Server storage check failed' + self._fmt_request(request))


class StoreInvalidScalarTypeError(ServerError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('' + self._fmt_request(request))


class TakeoutInitDelayError(FloodError):
    def __init__(self, request, **kwargs):
        self.seconds = int(kwargs.get('capture', 0))
        super(Exception, self).__init__('A wait of {seconds} seconds is required before being able to initiate the takeout'.format(seconds=self.seconds) + self._fmt_request(request))


class TakeoutInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The takeout session has been invalidated by another data export session' + self._fmt_request(request))


class TakeoutRequiredError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('You must initialize a takeout request first' + self._fmt_request(request))


class TempAuthKeyEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('No temporary auth key provided' + self._fmt_request(request))


class TimeoutError(RPCErrorNeg503):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('A timeout occurred while fetching data from the bot' + self._fmt_request(request))


class TmpPasswordDisabledError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The temporary password is disabled' + self._fmt_request(request))


class TokenInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided token is invalid' + self._fmt_request(request))


class TtlDaysInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided TTL is invalid' + self._fmt_request(request))


class TypesEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The types field is empty' + self._fmt_request(request))


class TypeConstructorInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The type constructor is invalid' + self._fmt_request(request))


class UnknownMethodError(ServerError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The method you tried to call cannot be called on non-CDN DCs' + self._fmt_request(request))


class UrlInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("The URL used was invalid (e.g. when answering a callback with an URL that's not t.me/yourbot or your game's URL)" + self._fmt_request(request))


class UsernameInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Nobody is using this username, or the username is unacceptable. If the latter, it must match r"[a-zA-Z][\\w\\d]{3,30}[a-zA-Z\\d]"' + self._fmt_request(request))


class UsernameNotModifiedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The username is not different from the current username' + self._fmt_request(request))


class UsernameNotOccupiedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The username is not in use by anyone else yet' + self._fmt_request(request))


class UsernameOccupiedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The username is already taken' + self._fmt_request(request))


class UsersTooFewError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Not enough users (to create a chat, for example)' + self._fmt_request(request))


class UsersTooMuchError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The maximum number of users has been exceeded (to create a chat, for example)' + self._fmt_request(request))


class UserAdminInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("You're not an admin" + self._fmt_request(request))


class UserAlreadyParticipantError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The authenticated user is already a participant of the chat' + self._fmt_request(request))


class UserBannedInChannelError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("You're banned from sending messages in supergroups/channels" + self._fmt_request(request))


class UserBlockedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('User blocked' + self._fmt_request(request))


class UserBotError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Bots can only be admins in channels.' + self._fmt_request(request))


class UserBotInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('This method can only be called by a bot' + self._fmt_request(request))


class UserBotRequiredError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('This method can only be called by a bot' + self._fmt_request(request))


class UserChannelsTooMuchError(ForbiddenError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('One of the users you tried to add is already in too many channels/supergroups' + self._fmt_request(request))


class UserCreatorError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("You can't leave this channel, because you're its creator" + self._fmt_request(request))


class UserDeactivatedError(UnauthorizedError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The user has been deleted/deactivated' + self._fmt_request(request))


class UserIdInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Invalid object ID for a user. Make sure to pass the right types, for instance making sure that the request is designed for users or otherwise look for a different one more suited' + self._fmt_request(request))


class UserIsBlockedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('User is blocked' + self._fmt_request(request))


class UserIsBotError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("Bots can't send messages to other bots" + self._fmt_request(request))


class UserKickedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('This user was kicked from this supergroup/channel' + self._fmt_request(request))


class UserMigrateError(InvalidDCError):
    def __init__(self, request, **kwargs):
        self.new_dc = int(kwargs.get('capture', 0))
        super(Exception, self).__init__('The user whose identity is being used to execute queries is associated with DC {new_dc}'.format(new_dc=self.new_dc) + self._fmt_request(request))


class UserNotMutualContactError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The provided user is not a mutual contact' + self._fmt_request(request))


class UserNotParticipantError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The target user is not a member of the specified megagroup or channel' + self._fmt_request(request))


class UserPrivacyRestrictedError(ForbiddenError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("The user's privacy settings do not allow you to do this" + self._fmt_request(request))


class UserRestrictedError(ForbiddenError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__("You're spamreported, you can't create channels or chats." + self._fmt_request(request))


class VideoContentTypeInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('The video content type is not supported with the given parameters (i.e. supports_streaming)' + self._fmt_request(request))


class WcConvertUrlInvalidError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('WC convert URL invalid' + self._fmt_request(request))


class WebpageCurlFailedError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Failure while fetching the webpage with cURL' + self._fmt_request(request))


class WebpageMediaEmptyError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('Webpage media empty' + self._fmt_request(request))


class YouBlockedUserError(BadRequestError):
    def __init__(self, request, **kwargs):
        super(Exception, self).__init__('You blocked this user' + self._fmt_request(request))


rpc_errors_dict = {
    'ABOUT_TOO_LONG': AboutTooLongError,
    'ACCESS_TOKEN_EXPIRED': AccessTokenExpiredError,
    'ACCESS_TOKEN_INVALID': AccessTokenInvalidError,
    'ACTIVE_USER_REQUIRED': ActiveUserRequiredError,
    'ADMINS_TOO_MUCH': AdminsTooMuchError,
    'API_ID_INVALID': ApiIdInvalidError,
    'API_ID_PUBLISHED_FLOOD': ApiIdPublishedFloodError,
    'ARTICLE_TITLE_EMPTY': ArticleTitleEmptyError,
    'AUTH_BYTES_INVALID': AuthBytesInvalidError,
    'AUTH_KEY_DUPLICATED': AuthKeyDuplicatedError,
    'AUTH_KEY_INVALID': AuthKeyInvalidError,
    'AUTH_KEY_PERM_EMPTY': AuthKeyPermEmptyError,
    'AUTH_KEY_UNREGISTERED': AuthKeyUnregisteredError,
    'AUTH_RESTART': AuthRestartError,
    'BANNED_RIGHTS_INVALID': BannedRightsInvalidError,
    'BOTS_TOO_MUCH': BotsTooMuchError,
    'BOT_CHANNELS_NA': BotChannelsNaError,
    'BOT_GROUPS_BLOCKED': BotGroupsBlockedError,
    'BOT_INLINE_DISABLED': BotInlineDisabledError,
    'BOT_INVALID': BotInvalidError,
    'BOT_METHOD_INVALID': BotMethodInvalidError,
    'BOT_MISSING': BotMissingError,
    'BOT_POLLS_DISABLED': BotPollsDisabledError,
    'BUTTON_DATA_INVALID': ButtonDataInvalidError,
    'BUTTON_TYPE_INVALID': ButtonTypeInvalidError,
    'BUTTON_URL_INVALID': ButtonUrlInvalidError,
    'CALL_ALREADY_ACCEPTED': CallAlreadyAcceptedError,
    'CALL_ALREADY_DECLINED': CallAlreadyDeclinedError,
    'CALL_OCCUPY_FAILED': CallOccupyFailedError,
    'CALL_PEER_INVALID': CallPeerInvalidError,
    'CALL_PROTOCOL_FLAGS_INVALID': CallProtocolFlagsInvalidError,
    'CDN_METHOD_INVALID': CdnMethodInvalidError,
    'CHANNELS_ADMIN_PUBLIC_TOO_MUCH': ChannelsAdminPublicTooMuchError,
    'CHANNELS_TOO_MUCH': ChannelsTooMuchError,
    'CHANNEL_INVALID': ChannelInvalidError,
    'CHANNEL_PRIVATE': ChannelPrivateError,
    'CHANNEL_PUBLIC_GROUP_NA': ChannelPublicGroupNaError,
    'CHAT_ABOUT_NOT_MODIFIED': ChatAboutNotModifiedError,
    'CHAT_ABOUT_TOO_LONG': ChatAboutTooLongError,
    'CHAT_ADMIN_INVITE_REQUIRED': ChatAdminInviteRequiredError,
    'CHAT_ADMIN_REQUIRED': ChatAdminRequiredError,
    'CHAT_FORBIDDEN': ChatForbiddenError,
    'CHAT_ID_EMPTY': ChatIdEmptyError,
    'CHAT_ID_INVALID': ChatIdInvalidError,
    'CHAT_INVALID': ChatInvalidError,
    'CHAT_NOT_MODIFIED': ChatNotModifiedError,
    'CHAT_RESTRICTED': ChatRestrictedError,
    'CHAT_SEND_GIFS_FORBIDDEN': ChatSendGifsForbiddenError,
    'CHAT_SEND_MEDIA_FORBIDDEN': ChatSendMediaForbiddenError,
    'CHAT_SEND_STICKERS_FORBIDDEN': ChatSendStickersForbiddenError,
    'CHAT_TITLE_EMPTY': ChatTitleEmptyError,
    'CHAT_WRITE_FORBIDDEN': ChatWriteForbiddenError,
    'CODE_EMPTY': CodeEmptyError,
    'CODE_HASH_INVALID': CodeHashInvalidError,
    'CODE_INVALID': CodeInvalidError,
    'CONNECTION_API_ID_INVALID': ConnectionApiIdInvalidError,
    'CONNECTION_DEVICE_MODEL_EMPTY': ConnectionDeviceModelEmptyError,
    'CONNECTION_LANG_PACK_INVALID': ConnectionLangPackInvalidError,
    'CONNECTION_LAYER_INVALID': ConnectionLayerInvalidError,
    'CONNECTION_NOT_INITED': ConnectionNotInitedError,
    'CONNECTION_SYSTEM_EMPTY': ConnectionSystemEmptyError,
    'CONTACT_ID_INVALID': ContactIdInvalidError,
    'DATA_INVALID': DataInvalidError,
    'DATA_JSON_INVALID': DataJsonInvalidError,
    'DATE_EMPTY': DateEmptyError,
    'DC_ID_INVALID': DcIdInvalidError,
    'DH_G_A_INVALID': DhGAInvalidError,
    'EMAIL_HASH_EXPIRED': EmailHashExpiredError,
    'ENCRYPTED_MESSAGE_INVALID': EncryptedMessageInvalidError,
    'ENCRYPTION_ALREADY_ACCEPTED': EncryptionAlreadyAcceptedError,
    'ENCRYPTION_ALREADY_DECLINED': EncryptionAlreadyDeclinedError,
    'ENCRYPTION_DECLINED': EncryptionDeclinedError,
    'ENCRYPTION_ID_INVALID': EncryptionIdInvalidError,
    'ENCRYPTION_OCCUPY_FAILED': EncryptionOccupyFailedError,
    'ENTITY_MENTION_USER_INVALID': EntityMentionUserInvalidError,
    'ERROR_TEXT_EMPTY': ErrorTextEmptyError,
    'EXPORT_CARD_INVALID': ExportCardInvalidError,
    'EXTERNAL_URL_INVALID': ExternalUrlInvalidError,
    'FIELD_NAME_EMPTY': FieldNameEmptyError,
    'FIELD_NAME_INVALID': FieldNameInvalidError,
    'FILE_ID_INVALID': FileIdInvalidError,
    'FILE_PARTS_INVALID': FilePartsInvalidError,
    'FILE_PART_0_MISSING': FilePart0MissingError,
    'FILE_PART_EMPTY': FilePartEmptyError,
    'FILE_PART_INVALID': FilePartInvalidError,
    'FILE_PART_LENGTH_INVALID': FilePartLengthInvalidError,
    'FILE_PART_SIZE_INVALID': FilePartSizeInvalidError,
    'FILEREF_UPGRADE_NEEDED': FilerefUpgradeNeededError,
    'FIRSTNAME_INVALID': FirstNameInvalidError,
    'GIF_ID_INVALID': GifIdInvalidError,
    'GROUPED_MEDIA_INVALID': GroupedMediaInvalidError,
    'HASH_INVALID': HashInvalidError,
    'HISTORY_GET_FAILED': HistoryGetFailedError,
    'IMAGE_PROCESS_FAILED': ImageProcessFailedError,
    'INLINE_RESULT_EXPIRED': InlineResultExpiredError,
    'INPUT_CONSTRUCTOR_INVALID': InputConstructorInvalidError,
    'INPUT_FETCH_ERROR': InputFetchErrorError,
    'INPUT_FETCH_FAIL': InputFetchFailError,
    'INPUT_LAYER_INVALID': InputLayerInvalidError,
    'INPUT_METHOD_INVALID': InputMethodInvalidError,
    'INPUT_REQUEST_TOO_LONG': InputRequestTooLongError,
    'INPUT_USER_DEACTIVATED': InputUserDeactivatedError,
    'INVITE_HASH_EMPTY': InviteHashEmptyError,
    'INVITE_HASH_EXPIRED': InviteHashExpiredError,
    'INVITE_HASH_INVALID': InviteHashInvalidError,
    'LANG_PACK_INVALID': LangPackInvalidError,
    'LASTNAME_INVALID': LastnameInvalidError,
    'LIMIT_INVALID': LimitInvalidError,
    'LOCATION_INVALID': LocationInvalidError,
    'MAX_ID_INVALID': MaxIdInvalidError,
    'MD5_CHECKSUM_INVALID': Md5ChecksumInvalidError,
    'MEDIA_CAPTION_TOO_LONG': MediaCaptionTooLongError,
    'MEDIA_EMPTY': MediaEmptyError,
    'MEDIA_INVALID': MediaInvalidError,
    'MEDIA_NEW_INVALID': MediaNewInvalidError,
    'MEDIA_PREV_INVALID': MediaPrevInvalidError,
    'MEMBER_NO_LOCATION': MemberNoLocationError,
    'MEMBER_OCCUPY_PRIMARY_LOC_FAILED': MemberOccupyPrimaryLocFailedError,
    'MESSAGE_AUTHOR_REQUIRED': MessageAuthorRequiredError,
    'MESSAGE_DELETE_FORBIDDEN': MessageDeleteForbiddenError,
    'MESSAGE_EDIT_TIME_EXPIRED': MessageEditTimeExpiredError,
    'MESSAGE_EMPTY': MessageEmptyError,
    'MESSAGE_IDS_EMPTY': MessageIdsEmptyError,
    'MESSAGE_ID_INVALID': MessageIdInvalidError,
    'MESSAGE_NOT_MODIFIED': MessageNotModifiedError,
    'MESSAGE_TOO_LONG': MessageTooLongError,
    'MSG_WAIT_FAILED': MsgWaitFailedError,
    'NEED_CHAT_INVALID': NeedChatInvalidError,
    'NEED_MEMBER_INVALID': NeedMemberInvalidError,
    'NEW_SALT_INVALID': NewSaltInvalidError,
    'NEW_SETTINGS_INVALID': NewSettingsInvalidError,
    'OFFSET_INVALID': OffsetInvalidError,
    'OFFSET_PEER_ID_INVALID': OffsetPeerIdInvalidError,
    'OPTIONS_TOO_MUCH': OptionsTooMuchError,
    'PACK_SHORT_NAME_INVALID': PackShortNameInvalidError,
    'PACK_SHORT_NAME_OCCUPIED': PackShortNameOccupiedError,
    'PARTICIPANTS_TOO_FEW': ParticipantsTooFewError,
    'PARTICIPANT_CALL_FAILED': ParticipantCallFailedError,
    'PARTICIPANT_VERSION_OUTDATED': ParticipantVersionOutdatedError,
    'PASSWORD_EMPTY': PasswordEmptyError,
    'PASSWORD_HASH_INVALID': PasswordHashInvalidError,
    'PEER_FLOOD': PeerFloodError,
    'PEER_ID_INVALID': PeerIdInvalidError,
    'PEER_ID_NOT_SUPPORTED': PeerIdNotSupportedError,
    'PERSISTENT_TIMESTAMP_EMPTY': PersistentTimestampEmptyError,
    'PERSISTENT_TIMESTAMP_INVALID': PersistentTimestampInvalidError,
    'PERSISTENT_TIMESTAMP_OUTDATED': PersistentTimestampOutdatedError,
    'PHONE_CODE_EMPTY': PhoneCodeEmptyError,
    'PHONE_CODE_EXPIRED': PhoneCodeExpiredError,
    'PHONE_CODE_HASH_EMPTY': PhoneCodeHashEmptyError,
    'PHONE_CODE_INVALID': PhoneCodeInvalidError,
    'PHONE_NUMBER_APP_SIGNUP_FORBIDDEN': PhoneNumberAppSignupForbiddenError,
    'PHONE_NUMBER_BANNED': PhoneNumberBannedError,
    'PHONE_NUMBER_FLOOD': PhoneNumberFloodError,
    'PHONE_NUMBER_INVALID': PhoneNumberInvalidError,
    'PHONE_NUMBER_OCCUPIED': PhoneNumberOccupiedError,
    'PHONE_NUMBER_UNOCCUPIED': PhoneNumberUnoccupiedError,
    'PHONE_PASSWORD_FLOOD': PhonePasswordFloodError,
    'PHONE_PASSWORD_PROTECTED': PhonePasswordProtectedError,
    'PHOTO_CONTENT_URL_EMPTY': PhotoContentUrlEmptyError,
    'PHOTO_CROP_SIZE_SMALL': PhotoCropSizeSmallError,
    'PHOTO_EXT_INVALID': PhotoExtInvalidError,
    'PHOTO_INVALID': PhotoInvalidError,
    'PHOTO_INVALID_DIMENSIONS': PhotoInvalidDimensionsError,
    'PHOTO_SAVE_FILE_INVALID': PhotoSaveFileInvalidError,
    'PHOTO_THUMB_URL_EMPTY': PhotoThumbUrlEmptyError,
    'PIN_RESTRICTED': PinRestrictedError,
    'PRIVACY_KEY_INVALID': PrivacyKeyInvalidError,
    'PTS_CHANGE_EMPTY': PtsChangeEmptyError,
    'QUERY_ID_EMPTY': QueryIdEmptyError,
    'QUERY_ID_INVALID': QueryIdInvalidError,
    'QUERY_TOO_SHORT': QueryTooShortError,
    'RANDOM_ID_DUPLICATE': RandomIdDuplicateError,
    'RANDOM_ID_INVALID': RandomIdInvalidError,
    'RANDOM_LENGTH_INVALID': RandomLengthInvalidError,
    'RANGES_INVALID': RangesInvalidError,
    'REG_ID_GENERATE_FAILED': RegIdGenerateFailedError,
    'REPLY_MARKUP_INVALID': ReplyMarkupInvalidError,
    'REPLY_MARKUP_TOO_LONG': ReplyMarkupTooLongError,
    'RESULT_TYPE_INVALID': ResultTypeInvalidError,
    'RIGHT_FORBIDDEN': RightForbiddenError,
    'RPC_CALL_FAIL': RpcCallFailError,
    'RPC_MCGET_FAIL': RpcMcgetFailError,
    'RSA_DECRYPT_FAILED': RsaDecryptFailedError,
    'SEARCH_QUERY_EMPTY': SearchQueryEmptyError,
    'SEND_MESSAGE_MEDIA_INVALID': SendMessageMediaInvalidError,
    'SEND_MESSAGE_TYPE_INVALID': SendMessageTypeInvalidError,
    'SESSION_EXPIRED': SessionExpiredError,
    'SESSION_PASSWORD_NEEDED': SessionPasswordNeededError,
    'SESSION_REVOKED': SessionRevokedError,
    'SHA256_HASH_INVALID': Sha256HashInvalidError,
    'SHORTNAME_OCCUPY_FAILED': ShortnameOccupyFailedError,
    'START_PARAM_EMPTY': StartParamEmptyError,
    'START_PARAM_INVALID': StartParamInvalidError,
    'STICKERSET_INVALID': StickersetInvalidError,
    'STICKERS_EMPTY': StickersEmptyError,
    'STICKER_EMOJI_INVALID': StickerEmojiInvalidError,
    'STICKER_FILE_INVALID': StickerFileInvalidError,
    'STICKER_ID_INVALID': StickerIdInvalidError,
    'STICKER_INVALID': StickerInvalidError,
    'STICKER_PNG_DIMENSIONS': StickerPngDimensionsError,
    'STORAGE_CHECK_FAILED': StorageCheckFailedError,
    'STORE_INVALID_SCALAR_TYPE': StoreInvalidScalarTypeError,
    'TAKEOUT_INVALID': TakeoutInvalidError,
    'TAKEOUT_REQUIRED': TakeoutRequiredError,
    'TEMP_AUTH_KEY_EMPTY': TempAuthKeyEmptyError,
    'Timeout': TimeoutError,
    'TMP_PASSWORD_DISABLED': TmpPasswordDisabledError,
    'TOKEN_INVALID': TokenInvalidError,
    'TTL_DAYS_INVALID': TtlDaysInvalidError,
    'TYPES_EMPTY': TypesEmptyError,
    'TYPE_CONSTRUCTOR_INVALID': TypeConstructorInvalidError,
    'UNKNOWN_METHOD': UnknownMethodError,
    'URL_INVALID': UrlInvalidError,
    'USERNAME_INVALID': UsernameInvalidError,
    'USERNAME_NOT_MODIFIED': UsernameNotModifiedError,
    'USERNAME_NOT_OCCUPIED': UsernameNotOccupiedError,
    'USERNAME_OCCUPIED': UsernameOccupiedError,
    'USERS_TOO_FEW': UsersTooFewError,
    'USERS_TOO_MUCH': UsersTooMuchError,
    'USER_ADMIN_INVALID': UserAdminInvalidError,
    'USER_ALREADY_PARTICIPANT': UserAlreadyParticipantError,
    'USER_BANNED_IN_CHANNEL': UserBannedInChannelError,
    'USER_BLOCKED': UserBlockedError,
    'USER_BOT': UserBotError,
    'USER_BOT_INVALID': UserBotInvalidError,
    'USER_BOT_REQUIRED': UserBotRequiredError,
    'USER_CHANNELS_TOO_MUCH': UserChannelsTooMuchError,
    'USER_CREATOR': UserCreatorError,
    'USER_DEACTIVATED': UserDeactivatedError,
    'USER_ID_INVALID': UserIdInvalidError,
    'USER_IS_BLOCKED': UserIsBlockedError,
    'USER_IS_BOT': UserIsBotError,
    'USER_KICKED': UserKickedError,
    'USER_NOT_MUTUAL_CONTACT': UserNotMutualContactError,
    'USER_NOT_PARTICIPANT': UserNotParticipantError,
    'USER_PRIVACY_RESTRICTED': UserPrivacyRestrictedError,
    'USER_RESTRICTED': UserRestrictedError,
    'VIDEO_CONTENT_TYPE_INVALID': VideoContentTypeInvalidError,
    'WC_CONVERT_URL_INVALID': WcConvertUrlInvalidError,
    'WEBPAGE_CURL_FAILED': WebpageCurlFailedError,
    'WEBPAGE_MEDIA_EMPTY': WebpageMediaEmptyError,
    'YOU_BLOCKED_USER': YouBlockedUserError,
}

rpc_errors_re = (
    ('EMAIL_UNCONFIRMED_(\\d+)', EmailUnconfirmedError),
    ('FILE_MIGRATE_(\\d+)', FileMigrateError),
    ('FILE_PART_(\\d+)_MISSING', FilePartMissingError),
    ('FLOOD_TEST_PHONE_WAIT_(\\d+)', FloodTestPhoneWaitError),
    ('FLOOD_WAIT_(\\d+)', FloodWaitError),
    ('INTERDC_(\\d+)_CALL_ERROR', InterdcCallErrorError),
    ('INTERDC_(\\d+)_CALL_RICH_ERROR', InterdcCallRichErrorError),
    ('NETWORK_MIGRATE_(\\d+)', NetworkMigrateError),
    ('PHONE_MIGRATE_(\\d+)', PhoneMigrateError),
    ('TAKEOUT_INIT_DELAY_(\\d+)', TakeoutInitDelayError),
    ('USER_MIGRATE_(\\d+)', UserMigrateError),
)
