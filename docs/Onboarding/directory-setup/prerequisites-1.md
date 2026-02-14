---
title: Before You Begin
excerpt: >-
  To use OpenDOOR features, we must first define the **directory structure** of
  your organization and properties.
deprecated: false
hidden: false
metadata:
  robots: index
next:
  description: >-
    Review the Example Directory Structure, which will be used throughout this
    guide. Then proceed to set up a new property.
---
The **directory** is a hierarchical representation of the following information:

* 🗂️ **Account** (the root of your organization's directory)
  * 💼 Portfolios
    * 🏬 Properties
      * 🏢 Buildings (_optional_)
        * 1️⃣ Floors (_optional_)
          * 🏠 Units
            * 🚪 **Entrances**
            * Rooms (_optional_)

Other types of directory items may be used _at all levels_; the structure should be defined so that it accommodates your own requirements. For example, portfolios may represent geographical regions themselves, but they can also represent a single city of zip code, in which case they could also be _grouped_ under other directory items representing the region.

The topmost directory items, such as portfolios and properties, should closely mirror **your organisational structure**. For example, if your organisation has regional managers, then your directory should contain items for each region.

The subsequent directory items should closely mirror **the physical layout** of your buildings. They can be created based on the blueprint of a building. These items represent a _small subset_ of the building's digital twin; in particular, it is the subset of information required to enable **access** to the spaces within your building. You _may_ model your entire building as a directory, but you can also stop much earlier, depending on your exact use cases for OpenDOOR.

The directory items determine the **scope** of any roles assigned to your users; for example:

* Portfolio Managers will be granted administrative permissions for one of your 💼 Portfolio directory items;
* Property Managers will be granted administrative permissions for one of your 🏬 Property directory items;
* Residents will be granted access and related permissions for one of your 🏠 Unit directory items.

Consequently, it is important to consider your organisational structure _and business model_ when designing the layout of the directory. Your DOOR Sales Representative will assist you with this initial analysis.
