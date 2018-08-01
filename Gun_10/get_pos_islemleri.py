from requests import get, post, put, delete, patch
from pprint import pprint
from json import dumps

class ReqresApi:
    def __init__(self):
        self.url = "https://reqres.in/api/users"


    def kullanicilari_listele(self):
        resp = get(self.url)
        if resp.status_code==HTTPStatus.OK:
            return resp.json()
        return ({"hata":"istek hatalı"})

    def kullanici_ekle(self,isim,meslek):
        resp = post(self.url, data={'name':isim,
                                    'job':meslek})
        if resp.status_code==HTTPStatus.CREATED:
            return resp.json()
        return dumps({"hata":"istek hatalı"})

     def guncelle(self,isim, meslek,user_id):
         resp = patch(self.url + user_id, data = {'name':isim,
                                       'job':meslek})
         if resp.status_code==HTTPStatus.OK

    def sil(self,user_id):
        resp = delete(self.url + user_id)
        if resp.status_code == HTTPStatus.NO_CONTENT:
            return "başarılı"
        return dumps({"hata": "istek hatalı"})

if __name__ == '__main__':
    benim_apim = ReqresApi()
    pprint(benim_apim.kullanicilari_listele())