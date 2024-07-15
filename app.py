from flask import Flask, request, jsonify
from follower_system import FollowerSystem, User

app = Flask(__name__)
follower_system = FollowerSystem()

# API endpoint to follow a user


@app.route('/follow', methods=['POST'])
def follow_user():
    data = request.json
    follower = data.get('follower')
    following = data.get('following')

    follower_system.follow(follower, following)

    return jsonify({'message': 'You are now following {}.'.format(following)})

# API endpoint to unfollow a user


@app.route('/unfollow', methods=['POST'])
def unfollow_user():
    data = request.json
    follower = data.get('follower')
    following = data.get('following')

    follower_system.unfollow(follower, following)

    return jsonify({'message': 'You have unfollowed {}.'.format(following)})

# API endpoint to get daily follower count for a user


@app.route('/daily_follower_count/<username>', methods=['GET'])
def get_daily_follower_count(username):
    count = follower_system.get_daily_follower_count(username)

    return jsonify({'username': username, 'daily_follower_count': count})

# API endpoint to get common followers between two users


@app.route('/common_followers', methods=['GET'])
def get_common_followers():
    user1 = request.args.get('user1')
    user2 = request.args.get('user2')

    common_followers = list(follower_system.get_common_followers(user1, user2))

    return jsonify({'user1': user1, 'user2': user2, 'common_followers': common_followers})


if __name__ == '__main__':
    app.run(debug=True)
