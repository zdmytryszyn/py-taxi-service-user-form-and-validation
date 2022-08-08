# Taxi service user form and validation

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

In this task, you will implement a custom form and django built-in forms to create,
update or delete content from the site.

1. Implement:
    - `Create`, `Delete` views for `Driver`, 
2. On the driver list page create a button that leads to the driver creation page.
3. Create a driver's license update page. The form on this page must check that 
license:
    - Consist only of 8 characters
    - First 3 characters are uppercase letters
    - Last 5 characters are digits
4. On the driver detail page add buttons that lead to the driver's license updating page and
driver deletion page.
5. On the car detail page add button `Assign me to this car`. This button adds 
current user to car drivers. When current user is already a driver of this car, 
there should be `Delete me from this car` button that deletes user from car drivers.

The car detail page should look like this:
![image](https://mate-academy-images.s3.eu-central-1.amazonaws.com/django-forms-1.png)
![image](https://mate-academy-images.s3.eu-central-1.amazonaws.com/django-forms-2.png)

NOTE: Attach screenshots of all created or modified pages to pull request. It's important to attach images not links to them.
