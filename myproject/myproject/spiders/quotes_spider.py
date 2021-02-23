import scrapy

class QuotesSpider(scrapy.Spider):
	name = 'quotes_spider'

	def start_request(self):

		urls = [
			'http://www.dmoz.org/Computers/Programming/Languages/Python/Books/',
		    'http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/'
		]

		#Generator Function
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)


	def parse(self, response):
		page = response.url.split("/")[-2]
		filename = 'quotes-%s.html' % page
		with open(filename, 'wb') as f:
			f.write(response.body)
		self.log('Saved file %s' % filename)