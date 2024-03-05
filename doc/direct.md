Here are the endpoint URLs and HTTP methods for direct app:

### Messages

- **List**: `GET /api/direct/messages/`
    - Lists messages where the authenticated user is either the sender or the receiver, ordered by creation date in
      descending order.
- **Create**: `POST /api/direct/messages/`
    - Allows the authenticated user to create a new message, automatically setting the sender to the authenticated user.
- **Retrieve**: `GET /api/direct/messages/{pk}/`
    - Retrieves a specific message by its primary key (pk) if the authenticated user is either the sender or the
      receiver.
- **Update**: `PUT /api/direct/messages/{pk}/` or `PATCH /api/direct/messages/{pk}/`
    - Updates a specific message by its primary key (pk) if the authenticated user is the owner (sender) of the message.
- **Destroy**: `DELETE /api/direct/messages/{pk}/`
    - Deletes a specific message by its primary key (pk) if the authenticated user is the owner (sender) of the message.

This endpoint documentation is based on the `ModelViewSet` class functionality, which provides a full set of CRUD
operations