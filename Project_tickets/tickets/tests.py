from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views
from .models import Team
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
