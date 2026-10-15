#import <UIKit/UIKit.h>

NSMutableArray<NSDictionary *> *localVersionList, *remoteVersionList;

@interface LauncherNavigationController : UINavigationController

@property(nonatomic) UIProgressView *progressViewMain, *progressViewSub;
@property(nonatomic) UILabel* progressText;

- (void)enterModInstallerWithPath:(NSString *)path hitEnterAfterWindowShown:(BOOL)hitEnter;
- (void)fetchLocalVersionList;
- (void)playDemo;
- (void)setInteractionEnabled:(BOOL)enable forDownloading:(BOOL)downloading;

@end
