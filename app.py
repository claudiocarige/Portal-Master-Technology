import os
from mastertechnology import app

''' 
    *   PROJETO DE CRIAÇÃO DE SITE COM O MICRO-FRAMWORK FLASK   *
'''


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)