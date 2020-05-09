
Q: How do you run schema migrations in a serverless environment on AWS?

A: Use Cloudformation custom resources.

Cloudformation custom resources allow you to trigger a Lambda function at stack deployment time. For a primer on custom resources, check out this [blog](https://www.alexdebrie.com/posts/cloudformation-custom-resources/) by Alex Debrie.

Here's what you need

- A Lambda function to run the schema migration scripts against the RDS database.
- A Cloudformation custom resource to trigger the Lambda function at deployment time.

Because the schema migration is executed in a lambda function, you can use all the exiting ORM libraries you are familiar with.

In this repo, I use SQLAlchemy and Python.


## How to deploy

### Setup

Enter your AWS account credentials in the `~/.aws/credentials` file.
Create a new section for vfan credentials (see below for example)

```
[test_account]
aws_access_key_id = <YOUR_ACCESS_ID_HERE>
aws_secret_access_key = <YOUR_ACCESS_KEY_HERE>
region = us-west-2
```


### Deploy

#### Requirements

* Serverless Framework. Version 1.61.0 to 1.67.0
* Docker

In the root directory of each repository, use the following command to deploy.

`sls deploy -v --stage test --aws-profile test_account --region us-west-2`