from typing import Any, Dict, Optional, Union


class Whooks:

    def __init__(self, http: Any, validators: Any, utils: Any, api_key: str) -> None:
        self._http: Any = http
        self._api_key: str = api_key
        self._validators: Any = validators
        self._utils: Any = utils

    def get_hook_events(
        self,
        hook_id: int,
        start_id: Optional[int] = None,
        end_id: Optional[int] = None,
        only_failed: Optional[bool] = None,
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        _type: Optional[str] = None
    ) -> Dict[Any, Any]:
        api_key: Dict[str, str]
        validators: Dict[int, Dict[str, Any]]
        api_key, validators = self._utils.api_method_preprocessing(self)

        params: Dict[str, Union[str, int, bool]] = {
            'hook_id': hook_id
        }

        if start_id is not None:
            params.update({'start_id': start_id})

        if end_id is not None:
            params.update({'end_id': end_id})

        if only_failed is not None:
            params.update({'only_failed': only_failed})

        if limit is not None:
            params.update({'limit': limit})

        if skip is not None:
            params.update({'skip': skip})

        if _type is not None:
            params.update({'type': _type})

        self._utils.validate_data(self._validators.whooks.requests.get_hook_events, params)

        validators.update({200: self._validators.whooks.responses.get_hook_events})

        del params['hook_id']
        params.update(api_key)

        return self._http.get(url='/web-hooks/{}/events'.format(hook_id), params=params, validators=validators)
