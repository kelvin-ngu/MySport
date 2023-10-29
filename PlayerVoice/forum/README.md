All Community related API calls
=====================

This view is responsible for all the community related API calls required by the platform. All API calls should start with `/forum/{route}/`

Community APIs are listed below:
- [Get Posts By List](#get-post-list)
- [Get Post By ID](#get-post-by-id)
- [Create Post](#create-post) 
- [Create Comment](#create-comment)
- [Create Like](#create-like)
-----------------------

### Get Post List

To get a list of all posts

* Route: `post/`
* Method: GET

* Return:
```
    [
        {
            post: {
                id: uuid, (journal id)
                player: {
                    id: uuid, (player id)
                    username: str,
                    birth_year: int,
                    club: str,
                    role: str
                }
                rating: int,
                match_description: str,
                comment: str,
                created_at: datetime
            },
            likes: int,
            comments: [
                {
                    id: uuid (comment id),
                    comment: str,
                    post: uuid (post id),
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
        post: {
            id: uuid, (journal id)
            player: {
                id: uuid, (player id)
                username: str,
                birth_year: int,
                club: str,
                role: str
            }
            rating: int,
            match_description: str,
            comment: str,
            created_at: datetime
        },
        likes: int,
        comments: [
            {
                id: uuid (comment id),
                comment: str,
                post: uuid (post id),
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
    }
```


### Create Post

To create post

* Route: `post/`
* Method: POST
* Body (form data):
    * category: str
    * title: str
    * description: str
    * author: uuid

* Return:
```
    {
        post: {
            id: uuid, (journal id)
            player: {
                id: uuid, (player id)
                username: str,
                birth_year: int,
                club: str,
                role: str
            }
            rating: int,
            match_description: str,
            comment: str,
            created_at: datetime
        },
        likes: int,
        comments: [
            {
                id: uuid (comment id),
                comment: str,
                post: uuid (post id),
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
    }
```

### Create Comment

To create comment to a specific post

* Route: `post/{post_id}/comment/`
* Method: POST
* Body (form data):
    * comment: str
    * post: uuid
    * author: uuid

* Return:
```
    {
        id: uuid, (comment id)
        comment: str,
        post: uuid, (post id)
        author: uuid, (author id)
        created_at: datetime
    }
```

### Create Like

To create like to a specific post

* Route: `post/{post_id}/like/`
* Method: POST
* Body (form data):
    * post: uuid
    * author: uuid

* Return:
```
    {
        id: uuid, (like id)
        post: uuid, (post id)
        author: uuid, (author id)
        created_at: datetime
    }
```
