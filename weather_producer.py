url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=188e1deec8d666392172d438442b24ff"
response=requests.get(url)
print(response.text)
i=0
while True:
   p = Producer({'bootstrap.servers':'localhost:9092'})
   p.produce("Data_Streaming",response.text)
   p.flush()
   time.sleep(5)
   i+=1
   if i==200:
       break