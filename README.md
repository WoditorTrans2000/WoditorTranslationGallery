![BannerWODITOR](https://github.com/user-attachments/assets/e2d1f1ab-113e-440a-9391-6e9e5d0ad7de)

# Translation Gallery for WolfRPGEditor  

This repository contains translations for WolfRPGEditor

🇺🇸 en-US | 🇧🇷 pt-BR | 🇵🇹 pt-PT | 🇵🇱 pl-PL | 🇷🇺 ru | 🇰🇷 ko-KR

Other versions have yet to be added.

There is 2 goal of this repository:

- To be a place to archive translations of others translator, even is not complete.

- To translate WolfRPGEditor itself, from the previous or latest versions.

You won't find the program in the repository, only the resource files. But if you want to use the **translated Editor**, then check the [releases](https://github.com/WoditorTrans2000/WoditorTranslationGallery/releases).

## How the translations is done

There are two way to translate WolfRPGEditor:

### 1. By modifying the Editor.exe

By doing this way, you will have to translate all new or previous versions.
<br>This method is available in all versions, as you will be editing the program itself.<br>However, older versions cannot be totally translated and there is also a risk that they may get corrupted when edited.

Download the Editor [here](https://silversecond.com/WolfRPGEditor/Download.shtml)

### 2. By modifying the Editor.Lang.dll

Dll file contains all the WolfRPGEditor resources (menu, commands, string tables and etc.), when the file is on the same place as Editor.exe and open the Editor. All text will be replaced by the dll file.

This way, you can keep reusing the dll in other versions, but at some point it will stop working or some features will be missing. When this happens, you should update the dll. <br>However, the dll is not available in all versions, the oldest dll is from version 2.29X and there is also a risk of them being corrupted.

Download the dll [here](https://silversecond.com/WolfRPGEditor/Download.shtml#dll)

---

Please check the [credit](https://github.com/WoditorTrans2000/WoditorTranslationGallery#credit) to see what versions were made by which author.

If the authors don't want their translations here, please send an e-mail or open an issue. That way, I can remove the translation.

E-Mail: WoditorGameGallery@protonmail.com<br>I'm Brazilian! I can understand English, but not Japanese (Learning!)

[Discord](
https://discord.com/invite/c3F7fNyDKE) **WolfRPGEditor Hub** If you want to discuss about translations, please join the discord!

## Status

Currently only pt-BR and en-US are the one I'm updating when is necessary.

The version of the dll being translated and from the latest folder is 3.662.

🇧🇷 pt-BR - 100% - Sendo feito por [Woditortrans2000](https://github.com/WoditorTrans2000).


🇺🇸 en-US - 100% - Translation being done by [Yumu](https://github.com/yumunet)

## Contribution

As it's a very recent project, I'm still looking for a way for other people to contribute to the repository.

For now, this is the way to go if you've translated WolfRPGEditor into another language and it's not here. If you translated a language that didn't have a folder in the repository, make a fork and add the folder of said translation and, after that, do a pull request.

You can either complete the .rc that needs to be completed or use another translation to translate from another language. If you do this, give credit to the author of the translation you're using.

Let me know if you find a translation is not archived here. (Completed or not).

## How to use

If you want to translate the WolfRPGEditor to another language and want to use the .rc files from here.

First you need the following:

- A **Text editor** or an **IDE** to edit the .rc file.
- **Resource Hacker** or **RisohEditor** to add the .rc file translated to the dll.
- **Visual Studio** to adjust the UI.
- A software that allow the compare File and highlight diff. **(WinMerge and Meld.)**

### 1. Download the .rc files

First you need to download the .rc flies you want. In this case, let's say you want to translated the en-US to another language. [First download the MDS.rc file.](https://github.com/WoditorTrans2000/WoditorTranslationGallery/blob/main/Latest/en-US/MDS.rc)

![Download the .rc](https://github.com/user-attachments/assets/c6c662fd-d7b4-4c0c-b3d2-c5337b7480f6)

### 2. Modify the MDS.rc

Now open the .rc in your favorite text editor or IDE. You only need to translate the words in **"quotes"**. Don't change anything else, otherwise an error will occur when you compile the .rc in Resource Hacker.

### 3. Resource Hacker

When you have finished translating or want to test it, in **Resource Hacker** open the .rc and click on **compile(F5)**. When you do this, three folders will appear (Menu, Dialog and String Table) inside which there will be stars representing an element of WolfRPGEditor (Example: Dialog folder, star number 102 is the Show message command ).
> For those that use RisohEditor, the .rc will not open due the difference format. But the .rec can be open by both program.

![Show command](https://github.com/user-attachments/assets/10fa51bf-4c52-4d74-9e6b-ae17492b7b38)

In the Dialog you can adjust the UI if a text get chopped. However, I don't recommend that, because it can cause corruption and the extended styles to be deleted.
Instead, use [Visual studio to adjust UI](https://github.com/yumunet/WoditorTranslationGallery/wiki/Edit-dialog-boxes-with-Visual-Studio)(Credit:Yumunet).

When you finishing everything, click **Save (Ctrl+S)**. It gonna ask you if want saves as .rec or a .rc. Please choose the .rec one.

### 4. Translating the Dll

Now open the dll file (Make sure both .rec and dll are the same version.)
Do the following, **“Action” -> “Add from to resource file”**, choose the .rec we just saved. When you do this, a pop-up window will appear in which you can choose which resource will replace the following dll resource.

![Overwriting](https://github.com/user-attachments/assets/0e976625-528b-4f99-8d03-064496596f7b)

Finally, save the dll file. Now place the file in the same location as Editor.exe and run it. If the loading banner appears as **“Editor.lang.dll mode”**, it's working!

![Loading banner saying Editor.Lang.dll mode](https://github.com/user-attachments/assets/d3a0f5a7-d605-4e5c-9192-6c0e0236e471)

If not, then see the following solution:

> - The dll file is named "Editor.Lang.dll"?
> - Open an untranslated .dll and perform **“Action” -> “Add from to resource file”**, choose the translated .dll and replace only the Menu, Dialog and String Table. This may seem strange, but sometimes it works.

In the screenshot there's a missing font, this is because i using Linux not Windows, but you shouldn't have any problems if you use Windows.

### Updating the translation to a new version

If you want to update to a new version, do the following:

Create a new **blank script (Ctrl + N)** in the Resource Hacker, **“Action” -> “Add from to resource file”** choose the new version of the untranslated dll and then add the Menu, Dialog and String Table resources.

Now **“Action” -> “Save all resources to an .RC file** and name it something like ’MDS_(version number).rc” Do the same thing with the previous version of the dll.

> As an example let's say my current version is **3.613** and the new version is **3.617**, when you done all the stuff above, you will have a **MDS_3_613.rc** and a **MDS_3_617.rc**.

Then use software that allows you to compare files and show diff, such as **WinMerge**, **Meld** and like.<br>
You will compare the **previous .rc version** with the **new .rc version**. Now, note all the important differences, translate those parts and add them to the translated .rc.

![Meld](https://github.com/user-attachments/assets/c365b5a6-e846-412f-8813-1f2bea40b201)

And at the end, compile the .rc with the new parts, save it as .rec and add it to the new version of the dll.

<br>

That's basically all you need to understand, you also can do this with the exe not just dll! However, there are many things I haven't mentioned here, things related to some problems you may encounter. For this, I recommend checking out some [translation tips from Yumunet](https://github.com/yumunet/WoditorTranslationGallery/wiki).

## Social media

- Join the community of WolfRPGEditor !<br>When there's a release, I'll post it on all the social media below, if I can.

[ModDB](
https://www.moddb.com/groups/wolfrpgeditor-community) **- wolfrpgeditor -**
<br>Share games, discuss, art and other stuff.

[Reddit](
https://www.reddit.com/r/Udita_wolfrpgeditor/?rdt=34274) **-r/udita_wolfrpgeditor -**<br>Good place to share your devlog, but also the show ongoing project.

[Bluesky](
https://bsky.app/profile/woditorgamegallery.bsky.social) **- WoditorNews -**<br>
Where I post updates on translations in progress, sometimes I posts games by other developers.

## Credit

<p align="center">
    <img src="https://www.silversecond.net/banner/editor_banner.gif">

[WolfRPGエディター Main Page](https://silversecond.com/WolfRPGEditor/)<br>
[SmokingWOLF](https://github.com/smokingwolf)<br>
He is the developer of WolfRPGEditor and I would like to thank him for putting this repository on the main page!

<br/>

🇧🇷 pt-BR<br>
**(v3.39, v3.562, v3.555, v3.574, v3.613, v3.618, v3.626, v3.632 and v3.662)** translations by [Woditortrans2000](https://github.com/WoditorTrans2000) (Owner of this repository) personally, I prefer to be called **Oki**.

<br/>

🇺🇸 en-US<br/>
**(v3.613, v3.618, v3.626, v3.632 and v3.662)** Translation completed and improved by [Yumu](https://github.com/yumunet)<br>Previously, the translation used vgperson and Sugy's translation. But because of Yumu's contribution, it is now something of its own.<br> Also I would like to thank him for helping me with the repository and give me suggestion!

**(v1.10, v1.20, v1.30, v1.31, v3.562, v3.566 and v3.574)** Used Vgperson and Surgy to translate, with the addition of Woditortrans2000 and Yumu. However, the translation is out of date, so it needs to be updated.

**(v3.164)** by Surgy Search "wolf-rpg-editor-3-english" on f95zone. I didn't put the link because is a NSFW site.

**(v2.10 and v2.24)** Translations by [Vellena Himel(Vgperson)](http://vgperson.com/) and Edited by [Widderune](https://widderune.wixsite.com/widderune).

**(v2.02a)** Translation by chronodekar.<br>I didn't manage to find the original link to download.

<br/>

🇵🇹 pt-PT<br/>
**(v2.02a)** Translation by [makergame2000](https://centrorpg.com/index.php?topic=2586.0)<br>In the zip where the translation is included, there is also the translation (2.02a) eng Translation by chronodekar.

<br/>

🇵🇱 pl-PL<br/>
**(v3.39)** Part of the translation was taken from v2.264 by [Reptile](http://rpgmaker.pl/wrpge/).<br> There is no .rc for 2.264, as I couldn't save the resources as .rc.

<br/>

🇷🇺 ru<br/>
**(v3.39)** Part of the translation was taken from a screenshot by [Andy.Whitebird](https://rpgmaker.su/f55/wolf-rpg-editor-wrpge-%D0%9B%D0%BE%D0%BA%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F-3477/) where show his work in progress translation.<br> However, the Editor itself is lost.

<br/>

🇰🇷 kr-KR<br/>
**(v2.296, v3.14, v3.27, v3.39, v3.611, v3.613 and v3.632)** ko-KR translation by [Kamasun](https://sites.google.com/view/kamasun214/).<br>Placed here for archiving purposes.
