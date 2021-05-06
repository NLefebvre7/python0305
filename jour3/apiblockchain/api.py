# api python flask
# app.run()
# (password cypte sha256, username en clair)
# (qd il se connecte: token predefeni ou toute les requete avec username et mdp)

# note : authentification/blockchain testé/ #vendredi soutenance
# front:
import flask
from flask import redirect, url_for, request, jsonify, render_template, flash
import sqlite3
import json
from hashlib import sha256
from datetime import datetime







def calculateHash(block):
    bloc = str(block.index) + str(block.previoushash) + str(block.timestamp) + str(block.data) + str(block.nonce)
    return(sha256(bloc.encode('utf-8')).hexdigest())

#recoder
def repeat(string, length):
    return(string * (int(length/len(string))+1))[:length]

class Block(object):
    def __init__(self, index, previoushash, data):
        self.index = index
        self.previoushash = previoushash
        self.timestamp = datetime.now()
        self.data = data
        self.nonce = 0
        self.mineBlock()
# self.hash = mineblock, le rajouter ds la fonction mineblock

    def mineBlock(self):
        self.hash = calculateHash(self)
        zeros = "0000"#repeat("0", difficulty)
        self.nonce = 0
        while self.hash[0:4] != zeros:
            self.nonce += 1
            self.hash = calculateHash(self)

# class Blockchain(object):
#     def __init__(self):
#         self.blocks = []
    
#         genesisBlock = Block(0, None, "Genesis block")
#         self.blocks.append(genesisBlock)
    
#     def newBlock(self, data):
#         latestBlock = self.blocks[-1]
#         block = (Block(latestBlock.index + 1, latestBlock.hash, data))
#         self.blocks.append(block)



#     def isFirstBlockValid(self):
#         firstBlock = self.blocks[0]

#         if firstBlock.index != 0 and firstBlock.previousHash is not None and (firstBlock.hash is None or calculateHash(firstBlock) != firstBlock.hash) :
#             return False

#         return True

#concatener les 2 autres
    # def isValidBlock(self, block, previousBlock):
    #     if previousBlock.index+1 != block.index:
    #         return False

    #     if (block.previousHash is None or block.previousHash != previousBlock.hash):
    #         return False
        
    #     if (block.hash is None or calculateHash(block) != block.hash):
    #         return False
        
    #     return True
    
    # def isBlockchainValid(self):
    #     if not self.isFirstBlockValid():
    #         return False
        
    #     for i in range(1, len(self.blocks)):
    #         previousBlock = self.blocks[i-1]
    #         block = self.blocks[i]
    #         if previousBlock.index+1 != block.index and (block.previousHash is None or block.previousHash != previousBlock.hash) and (block.hash is None or calculateHash(block) != block.hash) :
    #             return False 

    #     return True
    
#recoder 
#     def writechain(self):
#         for block in self.blocks:
#             chain = "Ceci est le block a l'index:"+str(block.index)+"crée le : "+str(block.timestamp)+"\n le hash du block précédent celui ci est :"+str(block.previousHash)+" et il contient comme données: "+str(block.data)+"\n son hash est: "+str(block.hash)+"et le nombre de tentative est de : (nonce) "+str(block.nonce)+"\n"
#             #print(str(chain))
#             # f = open('storeblockchain'+str(block.index)+'.txt','wb')
#             # f.write("str(chain))
#             # f.close()
#             with open('testbc.txt', 'a') as file:
#               file.write(""+chain+"\n")



# bchain = Blockchain()

# blockn1 = bchain.newBlock("Second Block")


# blockn2 = bchain.newBlock("Third Block")


# blockn3 = bchain.newBlock("Fourth Block")


# bchain.isBlockchainValid()


# bchain.writechain()














app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/postblock', methods=['GET','POST'])
def add_block():
    conn = sqlite3.connect('block.db')

    


    if request.method == 'POST':
      

      #SELECT * FROM tablename ORDER BY column DESC LIMIT 1;
      index = 16   #conn.execute('SELECT index FROM blockchain ')#SELECT * FROM blokcchain ORDER BY column DESC LIMIT 1;    #request.form['index']# recupmerer de la base de donnée le dernier

      previoushash = "testqsssdd"# recupere de la bdd dernier hash
      data = request.form['data']
      timestamp = datetime.now()    
      nonce = 0
      
      
      block = (Block(index + 1, previoushash, data))
      print("\n\n\n"+str(block.index)+"\n\n\n")

      if not id:
          flash('error')
      else:
        conn = sqlite3.connect('block.db')
        conn.execute('''INSERT INTO blockchain ( `index`, previoushash, timestamp, data, nonce, hash ) VALUES(?,?,?,?,?,?)''', ( block.index, block.previoushash,block.timestamp,block.data,block.nonce,block.hash )) #tout mettre de block
        conn.commit()
        conn.close()
        return redirect("http://127.0.0.1:5000/blocks/all")
    return render_template('postblock.html')


    # sql = '''INSERT INTO blockchain(id, hash, previoushash)
    #             VALUES(?,?,?) '''
                
    # #blocks = (1, hash, previoushash)
    # cur = conn.cursor()

    # body = request.get_json()

    # data = json.loads(json.dumps(body))
    # testb = (data['id'], data['hash'], data['previoushash'])
    # #testb = ('7', 'hashtest', 'previoushashtest')
    # #print(data['author'])
    # #print(body)
    # cur.execute(sql, testb)




@app.route('/blocks/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('block.db')

    conn.row_factory = dict_factory
    
    cur = conn.cursor()

    all_blocks = cur.execute('SELECT * FROM blockchain;').fetchall()

    return jsonify(all_blocks)

path = 'E:\\IPSSI\\github\\python0305\\testbc.txt'
def display():
    file1 = open(path, 'r')
    Lines = file1.readlines()

    chain1 = " "
    for line in Lines:
        chain1 = chain1 + "{}".format(line.strip()) + "<br>"
    
    return chain1



 
# db = sqlalchemy()

# class User(db.Model):
#     __tablename__ = 'user'

#     email = db.Column(db.String, primary_key=True)
#     password = db.Column(db.String)
#     authenticated = db.Column(db.Boolean, default=False)

#     def email(self):
#         return self.email

#     def is_authenticated(self):
#         return self.authenticated



@app.route('/', methods=['GET'])
def home():
    return "<h1>NL & PL</h1><p>Voici vos blocks generé precedemment <br><br>"+display()+"</p>"


# app.secret_key = 'your secret key'
  
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'toor'
# app.config['MYSQL_DB'] = 'mysqldb'

# @app.route('/login', methods =['GET', 'POST'])
# def login():
#     msg = ''
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
#         username = request.form['username']
#         password = request.form['password']
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
#         account = cursor.fetchone()
#         if account:
#             session['loggedin'] = True
#             session['id'] = account['id']
#             session['username'] = account['username']
#             msg = 'Logged in successfully !'
#             return render_template('index.html', msg = msg)
#         else:
#             msg = 'Incorrect username / password !'
#     return render_template('login.html', msg = msg)

# @app.route('/register', methods =['GET', 'POST'])
# def register():
#     msg = ''
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
#         username = request.form['username']
#         password = request.form['password']
#         email = request.form['email']
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
#         account = cursor.fetchone()
#         if account:
#             msg = 'Account already exists !'
#         elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
#             msg = 'Invalid email address !'
#         elif not re.match(r'[A-Za-z0-9]+', username):
#             msg = 'Username must contain only characters and numbers !'
#         elif not username or not password or not email:
#             msg = 'Please fill out the form !'
#         else:
#             cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
#             mysql.connection.commit()
#             msg = 'You have successfully registered !'
#     elif request.method == 'POST':
#         msg = 'Please fill out the form !'
#     return render_template('register.html', msg = msg)



app.run()