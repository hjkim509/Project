from django.contrib.sessions.backends import db
from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/myreviews')
def my_reviews():
    return render_template('index02.html')


@app.route('/review', methods=['POST'])
def save_reviews():
    imageUrl_receive = request.form['imageUrl_give']
    title_receive = request.form['title_give']
    rating_receive = request.form['rating_give']
    comment_receive = request.form['comment_give']
    review_receive = request.form['review_give']

    doc = {
        'imageUrl': imageUrl_receive,
        'title': title_receive,
        'rating': rating_receive,
        'comment': comment_receive,
        'review': review_receive
    }

    db.review.insert_one(doc)

    return jsonify({'result': 'success', 'msg':'저장이 완료되었습니다!'})

@app.route('/reviews/list', methods=['GET'])
def read_reviews():
    result = list(db.review.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'reviews': result})


if __name__ == '__main__':
    app.run('0.0.0.0', port=6777, debug=True)