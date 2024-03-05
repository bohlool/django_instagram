Here are the endpoint URLs and HTTP methods, including custom actions for content app:

### Posts

- **List**: `GET /api/posts/`
    - Lists posts made by the authenticated user or by users they are following.
- **Create**: `POST /api/posts/`
    - Allows the authenticated user to create a new post, automatically setting the user to the authenticated user.
- **Retrieve**: `GET /api/posts/{pk}/`
    - Retrieves a specific post by its primary key (pk).
- **Update**: `PUT /api/posts/{pk}/` or `PATCH /api/posts/{pk}/`
    - Updates a specific post by its primary key (pk) if the authenticated user is the owner of the post.
- **Destroy**: `DELETE /api/posts/{pk}/`
    - Deletes a specific post by its primary key (pk) if the authenticated user is the owner of the post.

### Custom Actions on Posts

- **View Logs**: `GET /api/posts/{pk}/views/`
    - Retrieves view logs for a specific post.
- **Do Like**: `POST /api/posts/{pk}/do_like/`
    - Allows the authenticated user to like a specific post.
- **Likes**: `GET /api/posts/{pk}/likes/`
    - Lists likes for a specific post.
- **Do Comment**: `POST /api/posts/{pk}/do_comment/`
    - Allows the authenticated user to comment on a specific post. The comment text should be included in the request
      data.
- **Comments**: `GET /api/posts/{pk}/comments/`
    - Lists comments for a specific post.

### Stories

- **List**: `GET /api/stories/`
    - Lists stories made by the authenticated user or by users they are following, where `is_active` is `True`.
- **Create**: `POST /api/stories/`
    - Allows the authenticated user to create a new story, automatically setting the user to the authenticated user.
- **Retrieve**: `GET /api/stories/{pk}/`
    - Retrieves a specific story by its primary key (pk).
- **Update**: `PUT /api/stories/{pk}/` or `PATCH /api/stories/{pk}/`
    - Updates a specific story by its primary key (pk) if the authenticated user is the owner of the story.
- **Destroy**: `DELETE /api/stories/{pk}/`
    - Deletes a specific story by its primary key (pk) if the authenticated user is the owner of the story.

### Custom Actions on Stories

- **View Logs**: `GET /api/stories/{pk}/views/`
    - Retrieves view logs for a specific story.
- **Do Like**: `POST /api/stories/{pk}/do_like/`
    - Allows the authenticated user to like a specific story.
- **Likes**: `GET /api/stories/{pk}/likes/`
    - Lists likes for a specific story.

These endpoints and methods are derived from the `ModelViewSet` class functionality, which provides a full set of CRUD
operations.