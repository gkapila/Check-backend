from app import app

if __name__ == '__main__':
  PORT = 5003
  HOST = '0.0.0.0'
  print 'Server running on {}:{}'.format(HOST, PORT)
  app.run(host='0.0.0.0', port=5003)
