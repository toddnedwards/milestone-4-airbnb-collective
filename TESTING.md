# My AirBnB Collective - Testing

![Logo](readme_testing_media/my-airbnb-collective.jpeg)

[View Site](https://my-airbnb-collective-57b00b515cab.herokuapp.com/)
---

## Contents

* [Validation Testing](#validation-testing)
    * [HTML](#html)
    * [CSS](#css)
    * [Javascript](#javascript)
    * [Python](#python)
    * [Lighthouse](#lighthouse)
    * [Wave](#wave)
* [Manual Testing](#manual-testing)
    * [Testing User Stories](#testing-user-stories)
    * [Full Testing](#full-testing)

### Validation Testing
---

#### **HTML**

For all HTML validation I used [W3 Validator](https://validator.w3.org/)

---
**base.html / home.html**

When validating home page, I realised that there was a few problems concerning base.html.

With the favicon being given a bad value of 'favicon'. I switched the value instead to `<link rel="icon" type="image/png" href="{{ MEDIA_URL }}favicon.png">` which fixed the issue.

I also found an error with the meta tag, which showed a meta element with the http-equiv attribute whos value is X-UA-Compatible must have a content attribute with the value IE=edge.
The code was changed from `<meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">` to `<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">`. It appeared the .0 was causing the issue added to initial scale.

From validator I found a div that was added and the form was not closed. This was because the div was above the form:

![base.html div/form placement fail](readme_testing_media/html_validation/base.html_div_form_fail.png)

This was fixed by moving the div above the form and correcting the indentation:

![base.html div/form placement fixed](readme_testing_media/html_validation/base.html_div_form_fixed.png)

The last error was showing in base.html that I had added `type="text/javascript` in my postload js section. I removed this and passed all tests for base.html/ home.html

I added home.html to this section because these we're shown to me whilst viewing the home page. Once the errors we're removed in base.html, the home page showed no errors.

<details>
<summary>Issues</summary>
<br>
<img src="readme_testing_media/html_validation/html_check_home_fail.png" alt="base.html/ home.html issues">
</details>
<details>
<summary>Fixed</summary>
<br>
<img src="readme_testing_media/html_validation/html_check_home_fixed.png" alt="base.html/ home.html fixed">
</details>

---

**Properties.html**

Properties showed no HTML issues. **Passed**

![properties.html HTML passed](readme_testing_media/html_validation/properties_html_pass.png)

**faqs.html**

FAQs page showed `stray end tag div on line 179`, which can be seen here:

![FAQs stray end tag](readme_testing_media/html_validation/faqs_html_fail.png)

I realised this was because the container-fluid div on line 23 was closed with a `</div>` at the end. Once that was deleted, all tests we're passed

![FAQs html test passed](readme_testing_media/html_validation/faq_html_pass.png)

**Login.html**

Login showed no HTML issues. **Passed**

![properties.html HTML passed](readme_testing_media/html_validation/login_html_pass.png)

#### **CSS**

#### **Javascript**

#### **Python**

#### **Lighthouse**

#### **Wave**

### Manual Testing
---

#### **Testing User Stories**

#### **Full Testing**





