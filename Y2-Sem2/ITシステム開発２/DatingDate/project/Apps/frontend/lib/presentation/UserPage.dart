import 'dart:typed_data';

import 'package:dating_your_date/client/grpc_services.dart';
import 'package:dating_your_date/core/app_export.dart';
import 'package:dating_your_date/models/GlobalModel.dart';
import 'package:dating_your_date/pb/canChange.pb.dart';
import 'package:dating_your_date/pb/fix.pb.dart';
import 'package:dating_your_date/pb/rpc_socialmedia.pb.dart';
import 'package:dating_your_date/presentation/ChatBox.dart';
import 'package:dating_your_date/presentation/Profile/widgets/showDataBar.dart';
import 'package:dating_your_date/widgets/Custom_Show_Image.dart';
import 'package:dating_your_date/widgets/app_bar/Custom_App_bar.dart';
import 'package:dating_your_date/widgets/button/custom_outlined_button.dart';
import 'package:flutter/material.dart';
import 'package:grpc/grpc.dart';

class UserPage extends StatefulWidget {
  UserPage({super.key, this.canData, this.fixData, this.img, this.allImage, this.tType});

  final String? tType;
  final Fix? fixData;
  final Uint8List? img;
  final CanChange? canData;
  final List<Uint8List>? allImage;

  @override
  State<UserPage> createState() => _UserPageState();
}

class _UserPageState extends State<UserPage> {
  void checkSocialMediaRecode(BuildContext context) async {
    String? apiKeyU = await globalUserId.read(key: 'UserID');
    final userid = int.tryParse(apiKeyU!);
    try {
      final myReq = GetSocialMediaRequest(userID: userid, targetID: widget.canData!.userID);
      await GrpcChatService.client.getSocialMedia(myReq);
      final tarReq = GetSocialMediaRequest(userID: widget.canData!.userID, targetID: userid);
      await GrpcChatService.client.getSocialMedia(tarReq);
      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) =>
              ChatBox(name: widget.canData!.nickName, imageUrl: widget.img!, targetid: widget.canData!.userID, tType: widget.tType!),
        ),
      );
    } on GrpcError catch (e) {
      if (e.code == 5 || e.code == 13) {
        // my
        final mReq = CreateSocialMediaRequest(
          userID: userid,
          targetID: widget.canData!.userID,
          image: false,
          contact: false,
          appointment: false,
          sns: false,
          location: false,
        );
        await GrpcChatService.client.createSocialMedia(mReq);
        // target
        final tReq = CreateSocialMediaRequest(
          userID: widget.canData!.userID,
          targetID: userid,
          image: false,
          contact: false,
          appointment: false,
          sns: false,
          location: false,
        );
        await GrpcChatService.client.createSocialMedia(tReq);

        await Future.delayed(Duration(milliseconds: 300));
        checkSocialMediaRecode(context);
      }
      throw Exception("エラーがあります。$e");
    }
  }

  @override
  Widget build(BuildContext context) {
    MediaQueryData mediaQueryData = MediaQuery.of(context);
    double mediaH = mediaQueryData.size.height;
    double mediaW = mediaQueryData.size.width;
    return Scaffold(
      appBar: buildAppBar(context, "", true),
      backgroundColor: appTheme.bgColor,
      body: SingleChildScrollView(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            _buildImages(context, mediaH, mediaW),

            // name
            Text(
              widget.canData!.nickName + ',' + widget.fixData!.firstName,
              style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold, color: appTheme.black),
            ),
            // ago
            Text(widget.fixData!.age.toString() + ' 才', style: TextStyle(fontSize: 18, color: appTheme.black)),
            SizedBox(height: mediaH / 50),

            // Part 1
            Text("マイプロフィール", style: CustomTextStyles.infoTitle),
            _buildPart1(context, mediaH, mediaW),
            SizedBox(height: mediaH / 40),

            // Part 2
            Text("基本情報", style: CustomTextStyles.infoTitle),
            _buildPart2(context, mediaH, mediaW),
            SizedBox(height: mediaH / 40),

            // btn
            _buildNextButton(context),
            SizedBox(height: mediaH / 15),
          ],
        ),
      ),
    );
  }

  Widget _buildImages(BuildContext context, double mediaH, double mediaW) {
    return SizedBox(
      child: Container(
        height: mediaH / 6.5,
        child: ListView(
          scrollDirection: Axis.horizontal,
          children: [
            // far left
            SizedBox(width: mediaW / 25),
            // image
            _buildImageContainer(context, widget.allImage![0], mediaH, mediaW),
            if (widget.allImage!.length >= 2) _buildImageContainer(context, widget.allImage![1], mediaH, mediaW),
            if (widget.allImage!.length >= 3) _buildImageContainer(context, widget.allImage![2], mediaH, mediaW),
            if (widget.allImage!.length >= 4) _buildImageContainer(context, widget.allImage![3], mediaH, mediaW),
            if (widget.allImage!.length >= 5) _buildImageContainer(context, widget.allImage![4], mediaH, mediaW),
            // far right
            SizedBox(width: mediaW / 25),
          ],
        ),
      ),
    );
  }

  Widget _buildImageContainer(BuildContext context, Uint8List imageFile, double mediaH, double mediaW) {
    return InkWell(
      onTap: () {
        showDialog(
          context: context,
          builder: (context) => AlertDialog(content: Image(image: MemoryImage(imageFile))),
        );
      },
      child: Container(child: customImageDesign(context, imageFile, mediaH, mediaW)),
    );
  }

  /// Part 1
  Widget _buildPart1(BuildContext context, double mediaH, double mediaW) {
    return Padding(
      padding: EdgeInsets.symmetric(horizontal: mediaW / 10, vertical: mediaH / 30),
      child: Container(
        padding: EdgeInsets.all(20),
        decoration: BoxDecoration(
          color: Color.fromARGB(255, 233, 233, 233),
          borderRadius: BorderRadiusStyle.r15,
          boxShadow: [BoxShadow(color: appTheme.grey800.withOpacity(0.4), blurRadius: 5, offset: Offset(0, 4))],
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text("自己紹介", style: CustomTextStyles.showDataTitle),
            Container(decoration: BoxDecoration(border: Border(bottom: BorderSide(width: 1, color: appTheme.grey500)))),
            Text(widget.canData!.introduce, style: CustomTextStyles.smallTitle20),
            SizedBox(height: mediaH / 30),

            // gender
            ShownDataBarWidget(item: "性別", data: widget.fixData!.gender),
            SizedBox(height: mediaH / 40),

            // birth
            ShownDataBarWidget(item: "生年月日", data: widget.fixData!.birth),
            SizedBox(height: mediaH / 40),

            // constellations
            ShownDataBarWidget(item: "星座", data: widget.fixData!.constellation),
            SizedBox(height: mediaH / 40),

            // Country
            ShownDataBarWidget(item: "国籍", data: widget.fixData!.country),
            SizedBox(height: mediaH / 40),

            // blood
            ShownDataBarWidget(item: "血液型", data: widget.fixData!.blood),
            SizedBox(height: mediaH / 40),
          ],
        ),
      ),
    );
  }

  /// Part 2
  Widget _buildPart2(BuildContext context, double mediaH, double mediaW) {
    return Padding(
      padding: EdgeInsets.symmetric(horizontal: mediaW / 10, vertical: mediaH / 50),
      child: Container(
        padding: EdgeInsets.symmetric(horizontal: 20, vertical: 15),
        decoration: BoxDecoration(
          color: appTheme.grey100,
          borderRadius: BorderRadiusStyle.r15,
          boxShadow: [BoxShadow(color: appTheme.grey800.withOpacity(0.4), blurRadius: 5, offset: Offset(0, 4))],
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            // Nick Name
            ShownDataBarWidget(item: "ニックネーム", data: widget.canData!.nickName),
            SizedBox(height: mediaH / 40),

            // height
            ShownDataBarWidget(item: " 身長 - cm", data: widget.canData!.height.toString() + " CM"),
            SizedBox(height: mediaH / 40),

            // weight
            ShownDataBarWidget(item: " 体重 - kg", data: widget.canData!.weight.toString() + " KG"),
            SizedBox(height: mediaH / 40),

            // address
            ShownDataBarWidget(item: "居住地", data: widget.canData!.city),
            SizedBox(height: mediaH / 40),

            // education
            ShownDataBarWidget(item: "学歴", data: widget.canData!.education),
            SizedBox(height: mediaH / 40),

            // hobby
            ShownDataBarWidget(item: "趣味 - タイプ", data: widget.canData!.hobbyType),
            SizedBox(height: mediaH / 40),

            // hobby
            ShownDataBarWidget(item: "経験 - 年:", data: widget.canData!.experience.toString()),
            SizedBox(height: mediaH / 40),

            // job
            ShownDataBarWidget(item: "職種", data: widget.canData!.job),
            SizedBox(height: mediaH / 40),

            // sexual
            ShownDataBarWidget(item: "性的指向", data: widget.canData!.sexual),
            SizedBox(height: mediaH / 40),

            // sociability
            ShownDataBarWidget(item: "社交力", data: widget.canData!.sociability),
            SizedBox(height: mediaH / 40),

            // find target
            ShownDataBarWidget(item: "探す対象", data: widget.canData!.accompanyType),
            SizedBox(height: mediaH / 40),

            // religious
            ShownDataBarWidget(item: "宗教", data: widget.canData!.religious),
            SizedBox(height: mediaH / 100),
          ],
        ),
      ),
    );
  }

  Widget _buildNextButton(BuildContext context) {
    return CustomOutlinedButton(
      text: "チャット",
      onPressed: () {
        checkSocialMediaRecode(context);
      },
    );
  }
}
