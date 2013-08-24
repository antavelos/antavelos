from instagram.client import InstagramAPI

class Instapairs:

    def getPopularImages(self, imageType, count):   

        images = []
        api = InstagramAPI(client_id='e33a8515b0cc4bc8aef4e7b086b736b1', client_secret='b50e5753efaa40ff8953e24fb8126616')
        popular_media = api.media_popular(count=count)
        for media in popular_media:
            images.append(media.images[imageType].url)

        return images