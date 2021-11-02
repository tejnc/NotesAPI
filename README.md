## Notes API with User login

### Notes 

1. For adding notes to the database 
    api address: `<server-address>/dev/add ` , and method is POST.
    And the body parameters are :
        a. title
        b. description
        c. status  (pending,completed, incomplete)

2. For updating notes
    api address: `<server-address>/dev/update/note/{args}/{oid}`
    where oid is the ObjectId of note, and args can be:-
    - title or status or description 

    Method is PATCH
    And the body parameters are as per the args chosen

3. For updating the whole note
    api address: `<server-address>/dev/update/note/{oid}`
    where oid is the ObjectId of note,
    And the body parameters are :
        a. title
        b. description
        c. status (pending, completed, incomplete)

4. For deleting the note
    api address: `<server-address>/dev/note/delete/{oid}`
    where oid is the ObjectId of note,
    And Method is GET, selected note is deleted.

5. For adding likes
    api address: `<server-address>/dev/note/like/{oid}`
    where oid is the ObjectId of note,
    And Method is GET, like is added to the selected note.

6. For commenting
    api address: `<server-address>/dev/note/comment/{oid}`
    where oid is the ObjectId of note,
    body parameters are:
    - comment_stated
    - comment_by

### Users

1. For registering user
