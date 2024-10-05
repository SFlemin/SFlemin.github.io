---
layout: default
---


Hi there! 

Thank you for taking the time to look over my home projects. Here you will find a growing set of cybersecurity and networking ventures.



# Microsoft Sentinel Log Aggregation

Using Microsoft Azure, I ran a deliberately exposed Virtual Machine with RDP (port 3389) enabled. My aim was to detect remote login attempts and automate alerts through the Microsoft Sentinel SIEM tool. I set up the following log rules to automatically filter all events and set severity levels for each of them.

- Unsuccesful Logins (Medium)
- All Succssful Logins (Medium)

![Branching](Log Rule Filtering.JPG)


I was able to aggregate these remote login alerts from Azure Monitor Agent (and transfer them to Sentinel) and filter out all other events, to present them in the Sentinel Dashboard

## AMA Logs 
* * *
![Branching](Aggregated logs from windows to sentinel.JPG)



## Sentinel Dashboard Representation
* * *
![Branching](Sentinel Alert Dashboard.JPG)

# Virtual Home and Office Networks
***

Using Cisco Packet Tracer, I created and customised both a home and office network using the neccesary networking devices.


 
# Certifications
* * *
## CompTIA Security+
![Branching](CompTIA Security+ ce certificate-1_page-0001.jpg)

## Google Cybersecurity
![Branching](Google Cybersecuritry Certififcate-2_page-0001.jpg)



This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

Text can be **bold**, _italic_, ~~strikethrough~~ or `keyword`.

[Link to another page](./another-page.html).

There should be whitespace between paragraphs.

There should be whitespace between paragraphs. We recommend including a README, or a file with information about your project.

# Header 1

This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

## Header 2

> This is a blockquote following a header.
>
> When something is important enough, you do it even if the odds are not in your favor.

### Header 3

```js
// Javascript code with syntax highlighting.
var fun = function lang(l) {
  dateformat.i18n = require('./lang/' + l)
  return true;
}
```

```ruby
# Ruby code with syntax highlighting
GitHubPages::Dependencies.gems.each do |gem, version|
  s.add_dependency(gem, "= #{version}")
end
```

#### Header 4

*   This is an unordered list following a header.
*   This is an unordered list following a header.
*   This is an unordered list following a header.

##### Header 5

1.  This is an ordered list following a header.
2.  This is an ordered list following a header.
3.  This is an ordered list following a header.

###### Header 6

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |

### There's a horizontal rule below this.

* * *

### Here is an unordered list:

*   Item foo
*   Item bar
*   Item baz
*   Item zip

### And an ordered list:

1.  Item one
1.  Item two
1.  Item three
1.  Item four

### And a nested list:

- level 1 item
  - level 2 item
  - level 2 item
    - level 3 item
    - level 3 item
- level 1 item
  - level 2 item
  - level 2 item
  - level 2 item
- level 1 item
  - level 2 item
  - level 2 item
- level 1 item

### Small image

![Octocat](https://github.githubassets.com/images/icons/emoji/octocat.png)

### Large image

![Branching](Sentinel Alert Dashboard.JPG)


### Definition lists can be used with HTML syntax.

<dl>
<dt>Name</dt>
<dd>Godzilla</dd>
<dt>Born</dt>
<dd>1952</dd>
<dt>Birthplace</dt>
<dd>Japan</dd>
<dt>Color</dt>
<dd>Green</dd>
</dl>

```
Long, single-line code blocks should not wrap. They should horizontally scroll if they are too long. This line should be long enough to demonstrate this.
```

```
The final element.
```
