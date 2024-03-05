Here are the endpoint URLs and HTTP methods for the user_activities app:

### Likes

- **List**: `GET /api/user-activity/likes/`
    - Lists likes made by the authenticated user.
- **Create**: `POST /api/user-activity/likes/`
    - Allows the authenticated user to create a new like, automatically setting the user to the authenticated user.
- **Retrieve**: `GET /api/user-activity/likes/{pk}/`
    - Retrieves a specific like by its primary key (pk) if the authenticated user is the owner of the like.
- **Destroy**: `DELETE /api/user-activity/likes/{pk}/`
    - Deletes a specific like by its primary key (pk) if the authenticated user is the owner of the like.

### Comments

- **List**: `GET /api/user-activity/comments/`
    - Lists comments made by the authenticated user.
- **Create**: `POST /api/user-activity/comments/`
    - Allows the authenticated user to create a new comment, automatically setting the user to the authenticated user.
- **Retrieve**: `GET /api/user-activity/comments/{pk}/`
    - Retrieves a specific comment by its primary key (pk) if the authenticated user is the owner of the comment.
- **Update**: `PUT /api/user-activity/comments/{pk}/` or `PATCH /api/user-activity/comments/{pk}/`
    - Updates a specific comment by its primary key (pk) if the authenticated user is the owner of the comment.
- **Destroy**: `DELETE /api/user-activity/comments/{pk}/`
    - Deletes a specific comment by its primary key (pk) if the authenticated user is the owner of the comment.

These endpoints and methods are derived from the `ModelViewSet` class, which provides a complete set of CRUD operations.