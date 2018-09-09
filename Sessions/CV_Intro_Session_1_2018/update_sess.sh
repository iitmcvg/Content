git clone https://github.com/iitmcvg/Content.git
rm -rf /session
mv -r Content/Sessions/CV_Intro_Session_1_2018 / && rm -rf /Content
mv /CV_Intro_Session_1_2018 /session && chmod a+rwx /session 
echo "Session contents updated"