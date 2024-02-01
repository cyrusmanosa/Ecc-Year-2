import 'package:dating_your_date/core/app_export.dart';
import 'package:flutter/material.dart';

class CustomDropDownBar extends StatelessWidget {
  CustomDropDownBar({
    Key? key,
    this.alignment,
    this.borderDecoration,
    this.controller,
    this.contentPadding,
    this.fillColor,
    this.focusNode,
    this.hintText,
    this.hintStyle,
    this.initialValue,
    this.maxLines,
    this.maxLength,
    this.prefix,
    this.prefixConstraints,
    this.suffix,
    this.suffixConstraints,
    this.textStyle,
    this.width,
    this.height,
    this.validator,
    this.textInputAction,
    this.textInputType,
    this.autofocus = true,
    this.filled,
    this.obscureText,
    this.onTap,
    this.items,
    this.itemArray,
    this.value,
    this.onChanged,
  }) : super(key: key);

  final Alignment? alignment;
  final bool autofocus;
  final bool? filled;
  final bool? obscureText;
  final BoxConstraints? prefixConstraints;
  final BoxConstraints? suffixConstraints;
  final Color? fillColor;
  final double? width;
  final double? height;
  final EdgeInsets? contentPadding;
  final FocusNode? focusNode;
  final FormFieldValidator<String>? validator;
  final int? maxLines;
  final int? maxLength;
  final InputBorder? borderDecoration;
  final String? hintText;
  final String? initialValue;
  final TextEditingController? controller;
  final TextInputAction? textInputAction;
  final TextInputType? textInputType;
  final TextStyle? hintStyle;
  final TextStyle? textStyle;
  final Widget? prefix;
  final Widget? suffix;
  final VoidCallback? onTap;
  final List<DropdownMenuItem<String>>? items;
  final List<String>? itemArray;
  final String? value;
  final ValueChanged<String?>? onChanged;

  @override
  Widget build(BuildContext context) {
    MediaQueryData mediaQueryData = MediaQuery.of(context);
    double mediaH = mediaQueryData.size.height;
    double mediaW = mediaQueryData.size.width;
    return LayoutBuilder(
      builder: (context, constraints) {
        return SizedBox(
          height: height ?? mediaH / 25,
          width: width ?? mediaW / 1.2,
          child: DropdownButtonFormField(
            borderRadius: BorderRadiusStyle.r15,
            decoration: decoration,
            value: value,
            items: itemArray!.toSet().map((option) {
              return DropdownMenuItem(value: option, child: Text(option));
            }).toList(),
            onChanged: (value) {
              controller!.text = value!;
            },
            style: theme.textTheme.displayLarge,
          ),
        );
      },
    );
  }

  InputDecoration get decoration => InputDecoration(
        contentPadding: contentPadding ?? EdgeInsets.only(top: -30),
        hintText: hintText,
        hintStyle: theme.textTheme.bodySmall,
        isDense: false,
        prefix: prefix ?? Padding(padding: EdgeInsets.only(left: 15.0)),
        border: OutlineInputBorder(borderRadius: BorderRadiusStyle.r15, borderSide: BorderSide(width: 2)),
        focusedBorder: OutlineInputBorder(borderRadius: BorderRadiusStyle.r15, borderSide: BorderSide(color: appTheme.pinkA100, width: 2)),
      );
}
