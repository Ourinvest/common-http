# COMMOM-HTTP-FASTAPI

Project to use as submodule in FastApi solutions.

#### Directory and files 

Architeture of the project if given below.
```
├──common_http
    └──schemas.py
    └──definitions.py
    └──responses.py
```

While in the responses file there are methods defined to be used in the api routes, the other two contains definitions for the OpenAPI document generation.

- In the schemas.py file it is defined the structure of the possible responses, always thinking in a JSONResponse method;

- In the definitions.py there are dictionaries describing possible responses codes for each type of request [GET, POST, PUT, DELETE] and its definitions.
---
## Usage
#### Installation

The following command will install from the main branch. **Be careful**.

`pip install git+ssh://github.com/Ourinvest/common-http.git`

You can choose manually the branch too, using:

`pip install git+ssh://github.com/Ourinvest/common-http.git@<BRANCH_NAME>`

As this is private repository, correct authentication will be required (a.k.a Token). 

#### Returning responses

As stated, in the responses.py file there is the class <g>CustomResponse</g>, in which there are static methods to be called generating a specific response.

**Successes**

For success responses [2xx] it is returned a JSONResponse indicating its status code and a message given.

```Python
return CustomResponse.success('Request processed successfully')
```
Or even return customized responses giving its status code.
```Python
return CustomResponse.custom_response(222, 'This is fun!')
```

**Errors**

While for error responses [4xx or 5xx], it is raised an HTTPException indicating its given detail.

```Python
raise CustomResponse.bad_request('That was a bad bad request, sir!')
```
Or
```Python
raise CustomResponse.custom_error(567, 'WOW, that wasn\'t supposed to happen!')
```
