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

---

**Property_details.html**

Property details came back with errors mainly for trailing slashes, which I removed. These we're removed from all images, from daterangepicker.css, and a stray tag removed from line 235.
Type was also removed from all extra scripts too. The script tags we're also edited in the includes files for modal and datepicker scripts. After these we're fixed, all tests passed:

<details>
<summary>Issues</summary>
<br>
<img src="readme_testing_media/html_validation/html_check_property_details_fail.png" alt="property_details.html issues">
</details>
<details>
<summary>Fixed</summary>
<br>
<img src="readme_testing_media/html_validation/html_check_property_details_pass.png" alt="base.html/ home.html fixed">
</details>

---

**faqs.html**

FAQs page showed `stray end tag div on line 179`, which can be seen here:

![FAQs stray end tag](readme_testing_media/html_validation/faqs_html_fail.png)

I realised this was because the container-fluid div on line 23 was closed with a `</div>` at the end. Once that was deleted, all tests we're passed

![FAQs html test passed](readme_testing_media/html_validation/faq_html_pass.png)

---

**contact.html**

Contact showed no HTML issues. **Passed**

![properties.html HTML passed](readme_testing_media/html_validation/html_contact_pass.png)

---

**Login.html**

Login showed no HTML issues. **Passed**

![properties.html HTML passed](readme_testing_media/html_validation/login_html_pass.png)

---

**Register.html**

Register page showed `Element ul not allowed as child of element small in this context. (Suppressing further errors from this subtree.)`, which can be seen here:

![FAQs stray end tag](readme_testing_media/html_validation/faqs_html_fail.png)

I realised this was because the container-fluid div on line 23 was closed with a `</div>` at the end. Once that was deleted, all tests we're passed

![FAQs html test passed](readme_testing_media/html_validation/faq_html_pass.png)

---

**Profile.html**

Because profile requires the user to be logged in, I could not validate the HTML content from the URL. I had to use text input to check instead. 
This gave me errors but we're all linked to variables (`{{ }}`) and tags/ filters (`{% %}`) which I know we're formatted correctly so I classed this as passed as no HTML errors we're shown otherwise. The only other error was `Element head is missing a required instance of child element title.` but this had passed on previous URLs with the same format so I put it down to the interaction of django that the HTML validator was not seeing because of it being text input instead of URL to validate.

![Profile html test passed](readme_testing_media/html_validation/html_profile_pass.png)

---

**Cart.html - URL Validation**

With validation I could only validate an empty cart which showed up the error ` The type attribute is unnecessary for JavaScript resources.` as seen here:

![Cart.html attribute layout error](readme_testing_media/html_validation/html_cart_error.png)

This was found on line 121 of cart.html:

![Cart.html script code adjustment](readme_testing_media/html_validation/cart_script_error.png)

Once I removed `type="text/javascript"` all tests passed.

![Cart.html HTML validation passed](readme_testing_media/html_validation/html_cart_pass.png)

**Cart.html - Text Input Validation**

Because I could only check an empty cart with the URL, I decided to check again with text input. The errors it showed we're similar to profile.html only showing areas due to the tags, filters and variables being used within the code so I didn't see these to be an issue and concluded this also passed as the tags, filters and variables follow the correct layout.

![Cart.html HTML text input issues](readme_testing_media/html_validation/cart_text_input_errors.png)

---

**Checkout.html - URL Validation**

Checkout URL validation showed no HTML issues. **Passed**

![checkout.html HTML URL validation passed](readme_testing_media/html_validation/checkout_url_validation_pass.png)

**Checkout.html - Text Input Validation**

Because I could only check an empty checkout with the URL, I decided to check again with text input. The errors again we're all related to tags, filters and variables, so I ignored them, but discovered that my H1 heading wasn't closed, so I added the closure on line 

![Cart.html HTML text input issues](readme_testing_media/html_validation/cart_text_input_errors.png)

---

**Edit_property.html - URL Validation**

Checked URL validation showed one error which was a space at the end of an element:

`Info: Trailing slash on void elements has no effect and interacts badly with unquoted attribute values.

From line 133, column 3; to line 133, column 65

iv>↩↩  ↩  <input type="hidden" name="next" value="/properties/edit/2/" />↩  ↩  `

This appeared to be from django's property.id passing through for editing the property, and this appeared to be correct still so was left alone.

---

#### **CSS**

[W3C](https://jigsaw.w3.org/css-validator/) was used to validate CSS.

| File | Result | Evidence |
| :--- | :--- | :---: |
| static/base.css | Pass | [base.css](readme_testing_media/css_validation/base_css.png)|
| airbnb_properties/static/airbnb_properties/css/properties.css | Pass | [properties.css](readme_testing_media/css_validation/properties_css.png)|
| cart/static/cart/css/cart.css | Pass | [cart.css](readme_testing_media/css_validation/cart_css.png)|
| checkout/static/checkout/css/checkout.css | Pass | [checkout.css](readme_testing_media/css_validation/checkout_css.png)|

#### **Javascript**

[Code Beautify](https://codebeautify.org/jsvalidate) was used to validate Javascript.

| File | Result | Evidence |
| :--- | :--- | :---: |
| checkout/static/checkout/js/stripe_elements.js | One warning, but copied from [boutique Ado's code](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/de7ad2067ac1b5de37a4cd8b9f4ddf572a4bf6c7/checkout/static/checkout/js/stripe_elements.js) | [stripe.js](readme_testing_media/js_validation/stripe_js.png)|
| home/templates/home/index.html | Fail (missing semicolon) | [carousel_js_error.js](readme_testing_media/js_validation/home_js_error.png)|
| home/templates/home/index.html | Pass (semicolon added to line 55) | [carousel_js_fixed.js](readme_testing_media/js_validation/home_js_fixed.png)|
| airbnb_properties/templates/includes/date_picker_script.html | Pass | [date_picker_script.js](readme_testing_media/js_validation/date_picker_js.png)|
| airbnb_properties/templates/includes/date_picker_script.html | Pass | [date_picker_script.js](readme_testing_media/js_validation/date_picker_js.png)|
| airbnb_properties/templates/includes/lightbox_script.html | Fail (unnecessary semicolons) | [light_box_js_error.js](readme_testing_media/js_validation/light_box_script_js_error.png)|
| airbnb_properties/templates/includes/lightbox_script.html | Pass (extra semicolons removed)| [light_box_js_fixed.js](readme_testing_media/js_validation/light_box_script_js_fixed.png)|

#### **Python**

#### **Lighthouse**

#### **Wave**

### Manual Testing
---

#### **Testing User Stories**

#### **Full Testing**





