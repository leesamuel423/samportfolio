---
title: practicing safe tests
date: 2023-03-17
description: automating e2e testing with trydent...
---

Today, we are excited to announce the release of Trydent, a lightweight developer tool built from the ground up to automate the generation of Cypress test code, simplifying and streamlining the end-to-end (E2E) testing process for applications.

The primary purpose of Trydent is to help developers and quality assurance engineers easily generate Cypress test code, saving time and effort while ensuring comprehensive test coverage. With Trydent, developers can create tests quickly, detect issues earlier in the development process, and maintain high-quality code standards.

![Test Example]({{ assets_path }}/test-example.png)

## 👏 E2E 👏 Testing 👏 is 👏 Important 👏

E2E testing is used to evaluate the performance of an application or system throughout its entire workflow. This involves testing all the components and subsystems, simulating real-world scenarios to align with user goals. Despite the importance of E2E testing, the tedious nature of writing these tests often dissuades developers from incorporating E2E testing into their application development life cycle.

To address these challenges, we developed Trydent, a user-friendly solution designed to easily automate the generation of E2E tests. The simplicity of Trydent sets it apart from other tools. It eliminates the need for complex setups or installations by harnessing the user-friendly interface of Chrome Developer Tools. This makes E2E testing more accessible and less intimidating for developers.

We firmly believe that E2E testing is indispensable in the software development process. It enables the early detection of bugs, ensures code functionality, and instills confidence in the reliability of software. Our goal with Trydent is to empower developers of all skill levels to embrace E2E testing without unnecessary barriers.

### 🔨 How it works 🔨

Trydent was built with convenience in mind, so that developers can get started with a few clicks of the mouse. All users have to do is either open their dev tools and navigate to the Trydent panel, or for user convenience, right click the page and choose Trydent. Instructions are written out within the app itself but below will also provide a high level overview:

![Trydent Demo]({{ assets_path }}/trydent-demo.gif)

To begin generating tests, all it takes is a simple click on the `New Test` button. Once recording, users can navigate through their website as normal, performing clicks, inputs, navigations and assertions. A final click on `Stop Recording & Generate Test` will create all the E2E cypress code for the user workflow. Users can copy the code and paste it directly into a cypress directory. Without any changes or typing, by implementing Trydent’s E2E tests, users can rest assured their applications will benefit from increased reliability and security.

A standout feature of Trydent is its ability to record Cypress assertions directly within Chrome. This feature is essential for E2E testing as it allows the verification of behavior and state of elements within an application while creating tests. By accurately reflecting the expected behavior and state of an application, Trydent facilitates more robust and reliable E2E testing.

## 🚗 Under the hood 🚗

![Architecture Diagram]({{ assets_path }}/architecture.png)

### 🔍 Monitoring Activity 🔍

Developer tools work through a series of chrome API’s that works as a messaging system between Trydent, service worker, the injected content scripts, and the application. Upon clicking `start recording`, Trydent sends a script to monitor user activity on the application and sends messages containing information such as the event type, xPath, and any input changes. From there, information is stored until users click `stop test and generate code`, when finally Trydent translates these events into readable, executable cypress code and clears the data object. So now, how does Trydent track events?

### 🦞 Selectors 🦞

This leads us to Selectors. There are many types of selectors that could be used when recording events, including CSS, ARIA, Text, and PIERCE. Unfortunately, many of these selectors do not have adequate coverage.

Trydent has been built with XPath as the primary selector. xPath stands for XML Path Language which uses a non-XML syntax to provide a flexible way of addressing different parts of an XML document. Trydent uses, xPath to track user events such as assertions, input changes, and navigation events. The in-house xPath generator function aims to create a relative xPath based off of cypress recommended attributes like [`data-cy`, `data-test`, and `data-testid`] as well as normal `id`. However, if none of these attributes are available, an absolute xPath is generated.

It’s important to note that when using Trydent, developer discretion is advised. As versatile as xPath is, absolute xPath can be brittle, as a minor change in the DOM can cause tests to fail even though the application may not be broken. This is a common problem found in most recorders and we hope to address this in the future by implementing combinations of different selectors to provide the most extensive coverage possible.

Remember, it is always important to be mindful about giving proper attribute labels and determining what matters when asserting and what is meaningful to users. For more information, recommend diving deeper into the native Cypress documentation for more details about how Cypress tests work!

## 🌊 Tame your Testing 🌊

Join us on this exciting journey of seamless E2E testing. Visit our website at trydent.io and explore how Trydent can revolutionize your development process. Together, let’s make E2E testing a standard practice for your development life cycle to build robust and reliable software with ease.
