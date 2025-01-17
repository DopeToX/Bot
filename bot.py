#include <string>
#include <iostream>
#include <vector>

using namespace std;

class MediaFiles {
protected:
    string name;
    string author;
public:
    MediaFiles() {}
    MediaFiles(string nm, string auth) : name(nm), author(auth) {}
    string get_name() {
        return name;
    }
    string get_author() {
        return author;
    }
    virtual void get_info(){}
};

// Texts
class TextFile : public MediaFiles {
public:
    int page_count;
    TextFile(string nm, string author, int page_count) : MediaFiles(nm, author), page_count(page_count) {}
    int get_pc() {
        return page_count;
    }
};

class Book : public TextFile {
public:
    Book(string nm, string author, int page_count) : TextFile(nm, author, page_count) {}
    string get_book(){
        return "book";
    };
};

class Comix : public TextFile {
public:
    Comix(string nm, string author, int page_count) : TextFile(nm, author, page_count) {}
    string get_comix(){
        return "comix";
    };
};

// Audio
class AudioFile : public MediaFiles {
public:
    int volume;
    AudioFile(string nm, string auth, int vol) : MediaFiles(nm, auth), volume(vol) {}
    int get_volume() {
        return volume;
    }
};

class Music : public AudioFile {
public:
    Music(string nm, string auth, int vol) : AudioFile(nm, auth, vol) {}
};

class Record : public AudioFile {
public:
    Record(string nm, string auth, int vol) : AudioFile(nm, auth, vol) {}
};

// Video
class VideoFile : public MediaFiles {};
class Serial : public VideoFile {};
class PhoneVid : public VideoFile {};

// Photo's
class PhotoFile : public MediaFiles {};
class DownloadedP : public PhotoFile {};
class TookedPic : public PhotoFile {};

int main() {
    
    vector<Book*> BookVec;
    BookVec.push_back(new Book("World War", "Pidoras", 812));
    vector<Comix*> ComixVec;
    ComixVec.push_back(new Comix("chmooo i", "Gay", 3123));
    
    vector<Music*> MusicVec;
    MusicVec.push_back(new Music("Serega", "Pirat", 62));
    vector<Record*> RecordVec;
    RecordVec.push_back(new Record("John", "Doe", 50));
    
    vector<Serial*> SerialVec;
    SerialVec.push_back(new Serial());
    vector<PhoneVid*> PhoneVidVec;
    PhoneVidVec.push_back(new PhoneVid());
    
    vector<DownloadedP*> DownloadedPVec;
    DownloadedPVec.push_back(new DownloadedP());
    vector<TookedPic*> TookedPicVec;
    TookedPicVec.push_back(new TookedPic());


    return 0;
}