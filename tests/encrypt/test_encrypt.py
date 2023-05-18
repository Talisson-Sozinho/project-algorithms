import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    valid_message = "example"
    invalid_message = 10
    valid_key = 5
    invalid_key = "5"
    expected_message_with_key_not_in_message_position = valid_message[::-1]
    expected_message_with_odd_key = "axe_elpm"
    expected_message_with_even_key = "elp_maxe"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(valid_message, invalid_key)

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(invalid_message, valid_key)

    assert (
        encrypt_message(valid_message, 99)
        == expected_message_with_key_not_in_message_position
    )

    assert encrypt_message(valid_message, 3) == expected_message_with_odd_key
    assert encrypt_message(valid_message, 4) == expected_message_with_even_key
