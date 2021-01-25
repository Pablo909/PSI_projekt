from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views
from .models import Team, Client
from rest_framework import status
from django.utils.http import urlencode
from django import urls


class TeamTests(APITestCase):
    def post_team(self, name):
        url = reverse(views.TeamView.name)
        data = {'name': name}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_team(self):
        new_team_name = 'Bayern Monachium'
        response = self.post_team(new_team_name)
        print("PK {0}".format(Team.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert Team.objects.count() == 1
        assert Team.objects.get().name == new_team_name

    def test_update_team(self):
        team_name = 'Arsenal Londyn'
        response = self.post_team(team_name)
        url = urls.reverse(views.TeamDetails.name, None, {response.data['id']})
        updated_team_name = 'Arsenal FC'
        data = {'name': updated_team_name}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['name'] == updated_team_name

    def test_delete_team(self):
        new_team_name = 'Borussia Dortmund'
        response = self.post_team(new_team_name)
        url = urls.reverse(views.TeamDetails.name, None, {response.data['id']})
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_filter_team_by_name(self):
        team_name_one = 'Lech Poznan'
        team_name_two = 'Aston Villa'
        self.post_team(team_name_one)
        self.post_team(team_name_two)
        filter_by_name = {'name': team_name_one}
        url = '{0}?{1}'.format(reverse(views.TeamView.name), urlencode(filter_by_name))
        print(url)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == team_name_one

    def test_get_team_list(self):
        new_team_name = 'MKS Dzialdowo'
        self.post_team(new_team_name)
        url = reverse(views.TeamView.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == new_team_name

    def test_get_team(self):
        team_name = 'Chelsea FC'
        response = self.post_team(team_name)
        url = urls.reverse(views.TeamDetails.name, None, {response.data['id']})
        get_response = self.client.patch(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['name'] == team_name


class ClientTests(APITestCase):
    def post_client(self, first_name, second_name, phone_number, email):
        url = reverse(views.ClientView.name)
        data = {'first_name': first_name, 'second_name': second_name, 'phone_number': phone_number, 'email': email, }
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_client(self):
        new_client_first_name = 'Jan'
        new_client_second_name = 'Nowak'
        new_client_phone_number = '456123778'
        new_client_email = 'j.nowak123@gmail.com'
        response = self.post_client(new_client_first_name, new_client_second_name, new_client_phone_number,
                                    new_client_email)
        print("PK {0}".format(Client.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert Client.objects.count() == 1
        assert Client.objects.get().first_name == new_client_first_name
        assert Client.objects.get().second_name == new_client_second_name
        assert Client.objects.get().phone_number == new_client_phone_number
        assert Client.objects.get().email == new_client_email

