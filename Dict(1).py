users = {
    'mross': {
        'first': 'aditya',
        'last': 'deshpande',
        'location': 'SIT',
    },

    'hspectre': {
        'first': 'kshitij',
        'last': 'tripathi',
        'location': 'SIT',
    }
}

for username, user_info in users.items():
    print("\nUsername:" + username);
    full_name = user_info['first'] + " " + user_info['last'];
    location = user_info['location'];

    print("\tFull name: " + full_name.title());
    print("\tLocation:" + location.title());
