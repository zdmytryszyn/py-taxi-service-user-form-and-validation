from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.forms import DriverLicenseUpdateForm


class ValidLicenseNumberFormTests(TestCase):
    def test_validation_license_number_with_valid_data(self):
        test_license_number = "TES12345"
        form = DriverLicenseUpdateForm(
            data={"license_number": test_license_number}
        )
        self.assertTrue(form.is_valid())

    def test_length_of_license_number_should_be_not_more_than_8(self):
        test_license_number = "TES123456"
        form = DriverLicenseUpdateForm(
            data={"license_number": test_license_number}
        )
        self.assertFalse(form.is_valid())

    def test_length_of_license_number_should_be_not_less_than_8(self):
        test_license_number = "TES1234"
        form = DriverLicenseUpdateForm(
            data={"license_number": test_license_number}
        )
        self.assertFalse(form.is_valid())

    def test_first_3_characters_should_be_uppercase_letters(self):
        test_license_number = "TE123456"
        form = DriverLicenseUpdateForm(
            data={"license_number": test_license_number}
        )
        self.assertFalse(form.is_valid())

    def test_last_5_characters_should_be_be_digits(self):
        test_license_number = "TEST23456"
        form = DriverLicenseUpdateForm(
            data={"license_number": test_license_number}
        )
        self.assertFalse(form.is_valid())


class DriverViewsTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="admin.user",
            license_number="ADM12345",
            first_name="Admin",
            last_name="User",
            password="1qazcde3"
        )
        self.client.force_login(self.user)

    def test_update_driver_license_number_with_valid_data(self):
        test_license_number = "ADM22345"
        response = self.client.post(
            reverse(
                "taxi:driver-update",
                kwargs={"pk": self.user.id}
            ),
            data={"license_number": test_license_number}
        )
        self.assertEqual(response.status_code, 302)

    def test_update_driver_license_number_with_not_valid_data(self):
        test_license_number = "a5"
        response = self.client.post(
            reverse(
                "taxi:driver-update",
                kwargs={"pk": self.user.id}
            ),
            data={"license_number": test_license_number}
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_driver(self):
        driver = get_user_model().objects.create(
            username="not_admin.user",
            license_number="NOT12345",
            first_name="Not Admin",
            last_name="User",
            password="1qazcde3"
        )
        response = self.client.post(
            reverse("taxi:driver-delete", kwargs={"pk": driver.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            get_user_model().objects.filter(id=driver.id).exists()
        )
