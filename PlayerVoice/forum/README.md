All Community related API calls
=====================

This view is responsible for all the community related API calls required by the platform. All API calls should start with `/forum/{route}/`

Community APIs are listed below:
- [Get Posts By List](#get-post-list)
- [Get Post By ID](#get-post-by-id)
- [Create Post](#automated-create-review-room) 
-----------------------

### Get Post List

To get a list of all posts

* Route: `post/`
* Method: GET

* Return:
```
    [
        {
            id: uuid, (post id)
            title: str,
            description: str,
            author: {
                id: uuid, (player id)
                username: str,
                birth_year: int,
                club: str,
                role: str
            },
            created_at: datetime
        }
    ]
```

### Get Post By ID

To get a specific Post using ID

* Route: `post/{post_id}`
* Method: GET

* Return:
```
    {
        id: uuid, (post id)
        title: str,
        description: str,
        author: {
            id: uuid, (player id)
            username: str,
            birth_year: int,
            club: str,
            role: str
        },
        created_at: datetime
    }
```


### Create Post

To create post

* Route: `post/`
* Method: POST
* Body (form data):


* Return:
```
    {
        id: uuid, (post id)
        title: str,
        description: str,
        author: {
            id: uuid, (player id)
            username: str,
            birth_year: int,
            club: str,
            role: str
        },
        created_at: datetime
    }
```
