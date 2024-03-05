Here's a documentation of the endpoint URLs and HTTP methods for the user_profiles app:

### Register

- **Create**: `POST /api/profile/register/`
    - For registering new account

### Profiles

- **List**: `GET /api/profile/profiles/`
    - Lists all profiles.
- **Retrieve**: `GET /api/profile/profiles/{pk}/`
    - Retrieves a specific profile by its primary key (pk).
- **Update**: `PUT /api/profile/profiles/{pk}/` or `PATCH /api/profile/profiles/{pk}/`
    - Updates a specific profile by its primary key (pk) if the authenticated user is the owner of the profile.

### Custom Actions on Profiles

- **Posts**: `GET /api/profile/profiles/{pk}/posts/`
    - Retrieves posts associated with a specific profile. The visibility of the posts may depend on the permissions (
      e.g., if the profile is public, or if the requesting user is following the profile).
- **Stories**: `GET /api/profile/profiles/{pk}/stories/`
    - Retrieves stories associated with a specific profile. Similar visibility rules as posts may apply.
- **Following**: `GET /api/profile/profiles/{pk}/following/`
    - Lists profiles that the specific profile is following.
- **Followers**: `GET /api/profile/profiles/{pk}/followers/`
    - Lists profiles that are following the specific profile.

### Change Password

- **Update**: `PUT /api/profile/change-pass/` or `PATCH /api/profile/change-pass/`
    - For changing your password

### Change Account

- **Update**: `PUT /api/profile/change-account/` or `PATCH /api/profile/change-account/`
    - For changing your name and username
- **Destroy**: `DELETE /api/profile/change-account/`
    - For deleting your account.

### Following

- **List**: `GET /api/profile/following/`
    - For listing accounts that you are following
- **Retrieve**: `GET /api/profile/following/{pk}/`
- **Create**: `POST /api/profile/following/`
    - For sending follow requests
- **Destroy**: `DELETE /api/profile/following/{pk}/`
    - For deleting follow requests

### Followers

- **List**: `GET /api/profile/followers/`
    - For listing your followers and recent requests to follow you
- **Retrieve**: `GET /api/profile/followers/{pk}/`
- **Update**: `PUT /api/profile/followers/{pk}/` or `PATCH /api/profile/followers/{pk}/`
    - For accepting new follow
      requests
- **Destroy**: `DELETE /api/profile/followers/{pk}/`
    - For deleting followers and follow requests


